from __future__ import annotations

class TrieNode:
    def __init__(self, character=None):
        self.character = character
        self.children = {}
        self.is_terminal = False
    
    def add_child(self, node: TrieNode):
        """Adds a node to the collection of children."""
        self.children[node.character] = node
    
    def get_child_with(self, character: str) -> TrieNode:
        """Return the node with the given character value, or None if none exist."""
        return self.children.get(character)

    def has_children(self) -> bool:
        """Return whether or not the node has children."""
        return len(self.children) > 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        """Inserts a new word into the Trie."""
        current = self.root
        for character in word:
            child = current.get_child_with(character)
            if child:
                current = child
            else:
                new_node = TrieNode(character)
                current.add_child(new_node)
                current = new_node
        
        current.is_terminal = True

    def search(self, word: str) -> bool:
        """Returns whether or not a given word exists in the Trie."""
        leaf = self._traverse_word(word)
        return leaf is not None and leaf.is_terminal

    def delete(self, word: str):
        """Deletes a given word from the Trie."""
        current = self.root
        stack = []

        for character in word:
            # If we end up deleting a word that has a prefix present in the Trie,
            # we need to preserve that prefix. So we clear the stack of nodes to
            # delete whenever we encounter a terminal node.
            if current.is_terminal:
                stack.clear()

            stack.append(current)
            child = current.get_child_with(character)
            if not child:
                return
            current = child

        # If the last node in the word has children, that means that a longer
        # word exists in the Trie with the word we are deleting as a prefix.
        # In this case, we do not want to actually delete the nodes.
        if current.has_children():
            current.is_terminal = False
        else:
            i = len(word) - 1
            while i >= 0 and len(stack) > 0:
                parent = stack.pop()
                del parent.children[word[i]]
                i -= 1
    
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

    def _traverse_word(self, word: str) -> TrieNode:
        current = self.root
        for character in word:
            child = current.get_child_with(character)
            if not child:
                return None
            current = child
        
        return current