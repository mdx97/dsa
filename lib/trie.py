from __future__ import annotations
from typing import Callable

class TrieNode:
    def __init__(self, character='', count=1):
        self.character = character
        self.children = {}
        self.is_terminal = False
        self.count = count
    
    def add_child(self, node: TrieNode):
        """Adds a node to the collection of children."""
        self.children[node.character] = node
    
    def get_child_with(self, character: str) -> TrieNode | None:
        """Return the node with the given character value, or None if none exist."""
        return self.children.get(character)

    def has_children(self) -> bool:
        """Return whether or not the node has children."""
        return len(self.children) > 0

class Trie:
    def __init__(self):
        self.root = TrieNode(count=0)

    def search(self, word: str) -> bool:
        """Returns whether or not a given word exists in the Trie."""
        leaf = self.get_leaf(word)
        return leaf is not None and leaf.is_terminal

    def insert(self, word: str):
        """Inserts a new word into the Trie."""
        def callback(character, current):
            child = current.get_child_with(character)
            if child:
                child.count += 1
                return child
            new_node = TrieNode(character)
            current.add_child(new_node)
            return new_node
        
        leaf = self._traverse_word(word, callback)
        leaf.is_terminal = True

    def delete(self, word: str):
        """Deletes a given word from the Trie."""
        stack = []

        def callback(character, current):
            # If we end up deleting a word that has a prefix present in the Trie,
            # we need to preserve that prefix. So we clear the stack of nodes to
            # delete whenever we encounter a terminal node.
            if current.is_terminal:
                stack.clear()
            stack.append(current)
            return current.get_child_with(character)
        
        leaf = self._traverse_word(word, callback)

        # If the last node in the word has children, that means that a longer
        # word exists in the Trie with the word we are deleting as a prefix.
        # In this case, we do not want to actually delete the nodes.
        if leaf.has_children():
            leaf.is_terminal = False
        else:
            i = len(word) - 1
            while i >= 0 and len(stack) > 0:
                parent = stack.pop()
                del parent.children[word[i]]
                i -= 1
    
    def get_leaf(self, word: str) -> TrieNode | None:
        """Returns the leaf node of the given word in the Trie, if it exists."""
        return self._traverse_word(
            word,
            lambda character, current: current.get_child_with(character))

    def longest_prefix(self, word: str) -> str:
        """Returns the longest prefix of the given word, if one exists."""
        current = self.root
        prefix = ""
        last_terminal = -1

        for idx, character in enumerate(word):
            child = current.get_child_with(character)
            if not child:
                break
            if child.is_terminal:
                last_terminal = idx
            
            prefix += character
            current = child
        
        if last_terminal == -1:
            return None

        return prefix[:last_terminal + 1]

    def _traverse_word(self, word: str, callback: function) -> TrieNode | None:
        """
        Helper method for hooking into the traversal algorithm
        with custom callback functions.
        """
        current = self.root
        for character in word:
            current = callback(character, current)
            if not current:
                return None

        return current

# https://www.geeksforgeeks.org/find-all-shortest-unique-prefixes-to-represent-each-word-in-a-given-list/
def shortest_unique_prefix(trie: Trie) -> list[str]:
    """Returns a list of the shortest unique prefixes in the Trie."""
    prefixes = []

    def dfs(node: TrieNode, running_string: str):
        new_string = running_string + node.character
        if node.count == 1:
            prefixes.append(new_string)
            return

        for child in node.children.values():
            dfs(child, new_string)

    dfs(trie.root, "")
    return prefixes