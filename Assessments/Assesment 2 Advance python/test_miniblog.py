"""
Unit Tests for MiniBlog Models and Storage operations.
Verifies OOP constraints and file read/write functionality with robust assertion cases.
"""

import unittest
import os
import shutil
from main import User, Post

class TestMiniBlog(unittest.TestCase):
    def setUp(self):
        # Create a temporary posts directory for testing purposes
        self.test_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_posts")
        if not os.path.exists(self.test_dir):
            os.makedirs(self.test_dir)

    def tearDown(self):
        # Clean up temporary test posts directory
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_user_validation_success(self):
        """Verifies User instantiation works with valid names."""
        user = User("Alice Smith")
        self.assertEqual(user.username, "Alice Smith")

    def test_user_validation_empty(self):
        """Verifies User instantiation throws ValueError for empty names."""
        with self.assertRaises(ValueError) as ctx:
            User("   ")
        self.assertIn("Author name cannot be empty", str(ctx.exception))

    def test_user_validation_short(self):
        """Verifies User instantiation throws ValueError for extremely short names."""
        with self.assertRaises(ValueError) as ctx:
            User("A")
        self.assertIn("must be at least 2 characters", str(ctx.exception))

    def test_post_validation_success(self):
        """Verifies Post instantiation works with valid data."""
        user = User("John Doe")
        post = Post("My First Post", "Hello world from MiniBlog!", user)
        self.assertEqual(post.title, "My First Post")
        self.assertEqual(post.content, "Hello world from MiniBlog!")
        self.assertEqual(post.author, user)

    def test_post_validation_empty_title(self):
        """Verifies Post throws error on empty title."""
        user = User("John Doe")
        with self.assertRaises(ValueError) as ctx:
            Post("   ", "Some valid content", user)
        self.assertIn("Post title cannot be empty", str(ctx.exception))

    def test_post_validation_empty_content(self):
        """Verifies Post throws error on empty content."""
        user = User("John Doe")
        with self.assertRaises(ValueError) as ctx:
            Post("Title", "   ", user)
        self.assertIn("Post content cannot be empty", str(ctx.exception))

    def test_post_filename_generation(self):
        """Verifies file name sanitization logic."""
        user = User("Alice O'Reilly-Smith!")
        post = Post("Welcome, Everyone! (v1.0)", "Content here", user)
        # Expected: alice_oreilly-smith_welcome_everyone_v10.txt
        expected_filename = "alice_oreilly-smith_welcome_everyone_v10.txt"
        self.assertEqual(post.get_filename(), expected_filename)

    def test_post_save_and_load_success(self):
        """Verifies that posts can be successfully written to and read from disk."""
        user = User("Bob Builder")
        post = Post("Can We Fix It?", "Yes, we can!", user)
        
        # Save to disk
        post.save_to_file(self.test_dir)
        filename = post.get_filename()
        filepath = os.path.join(self.test_dir, filename)
        
        self.assertTrue(os.path.exists(filepath))
        
        # Load from disk
        loaded_post = Post.load_from_file(filepath)
        self.assertEqual(loaded_post.title, post.title)
        self.assertEqual(loaded_post.author.username, post.author.username)
        self.assertEqual(loaded_post.content, post.content)
        self.assertEqual(loaded_post.timestamp, post.timestamp)

    def test_post_load_file_not_found(self):
        """Verifies FileNotFoundError is raised when attempting to load a non-existent file."""
        non_existent_path = os.path.join(self.test_dir, "ghost.txt")
        with self.assertRaises(FileNotFoundError):
            Post.load_from_file(non_existent_path)

    def test_post_load_corrupted_file(self):
        """Verifies that loader raises exception when opening corrupted/incomplete files."""
        filepath = os.path.join(self.test_dir, "bad_post.txt")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("Corrupted content with no headers or structure")
            
        with self.assertRaises(ValueError):
            Post.load_from_file(filepath)

if __name__ == "__main__":
    unittest.main()
