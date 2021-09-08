from .trie import Trie
import unittest

class TestTrie(unittest.TestCase):
    def test_insert_search(self):
        trie = Trie()
        trie.insert('hello')
        trie.insert('world')
        self.assertTrue(trie.search('hello'))
        self.assertTrue(trie.search('world'))
        self.assertFalse(trie.search('foobar'))

    def test_insert_counts(self):
        counts = []
        def callback(character, current):
            counts.append(current.count)
            return current.get_child_with(character)
        
        trie = Trie()
        trie.insert('hello')
        trie.insert('hel')
        leaf = trie._traverse_word('hello', callback)

        # The callback does not run for the leaf value but we still
        # want to assert that its count value is correct.
        counts.append(leaf.count)

        # The callback will count the root node value as well,
        # which we do not care about.
        counts = counts[1:]

        self.assertListEqual([2, 2, 2, 1, 1], counts)
    
    def test_search_does_not_match_substring(self):
        trie = Trie()
        trie.insert('helloworldandallwhoinhabitit')
        trie.insert('helloworld')
        self.assertFalse(trie.search('hello'))
        self.assertFalse(trie.search('helloworldand'))
        self.assertTrue(trie.search('helloworld'))
        self.assertTrue(trie.search('helloworldandallwhoinhabitit'))

    def test_delete(self):
        trie = Trie()
        trie.insert('hello')
        trie.delete('hello')
        self.assertFalse(trie.search('hello'))

    def test_delete_substring(self):
        trie = Trie()
        trie.insert('hello')
        trie.insert('helloworld')
        trie.delete('hello')
        self.assertFalse(trie.search('hello'))
        self.assertTrue(trie.search('helloworld'))

    def test_delete_with_prefix_intact(self):
        trie = Trie()
        trie.insert('hello')
        trie.insert('helloworld')
        trie.delete('helloworld')
        self.assertFalse(trie.search('helloworld'))
        self.assertTrue(trie.search('hello'))
        self.assertTrue(not trie.get_leaf('hello').has_children())

    def test_longest_prefix(self):
        trie = Trie()
        trie.insert('hello')
        trie.insert('helloworld')
        self.assertEqual('helloworld', trie.longest_prefix('helloworld'))
        self.assertEqual('helloworld', trie.longest_prefix('helloworldandallwhoinhabitit'))
        self.assertIsNone(trie.longest_prefix('foobar'))

if __name__ == '__main__':
    unittest.main()