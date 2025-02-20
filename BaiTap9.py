class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary chứa các ký tự con
        self.endWord = False  # Đánh dấu kết thúc của một từ

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr_node = self.root
        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = TrieNode()
            curr_node = curr_node.children[char]
        curr_node.endWord = True

    def search(self, word):
        curr_node = self.root
        for char in word:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]
        return curr_node.endWord  # Trả về True/False

    def print_tree(self):
        self._print_tree(self.root, "")

    def _print_tree(self, node, current_prefix):
        if node.endWord:
            print(current_prefix)
        for char, child_node in node.children.items():
            self._print_tree(child_node, current_prefix + char)

    def start_with(self, prefix):
        curr_node = self.root
        for char in prefix:
            if char not in curr_node.children:
                return None
            curr_node = curr_node.children[char]
        return curr_node

    def find_all_words(self, node, curr_prefix):
        suggested_words = []
        if node.endWord:
            suggested_words.append(curr_prefix)
        for char, child_node in node.children.items():
            suggested_words.extend(self.find_all_words(child_node, curr_prefix + char))
        return suggested_words

    def auto_complete(self, prefix):
        current = self.start_with(prefix)
        if current is None:
            return []
        return self.find_all_words(current, prefix)


# Tạo cây Trie và thêm từ
trie = Trie()
word_list = ["cat", "banana", "obama", "car", "cow", "alibaba"]
for word in word_list:
    trie.insert(word)

# Test in cây Trie
print("Cấu trúc cây Trie:")
trie.print_tree()

# Test tìm kiếm từ
print("\nTìm kiếm 'cat':", trie.search("cat"))
print("Tìm kiếm 'cy':", trie.search("cy"))

# Test gợi ý từ (autocomplete)
prefix = "c"
suggested_words = trie.auto_complete(prefix)
print(f"\nGợi ý từ cho '{prefix}': {suggested_words}")
