#pragma once
#include <iterator>
#include <iostream>
#include <vector>
#include <fstream>

template<typename T, class container = std::vector<T>>
class Binary_Tree {
public:
	class iterator;
	Binary_Tree() {
		root = nullptr;
		length = 0;
	};
	~Binary_Tree() {
		clear();
	};

	// Read values from a container to a tree
	void read(const container& values) {
		for (auto i = values.begin(); i != values.end(); ++i) {
			insert(*i);
		}
	};
	
	// Clear all data from the tree
	void clear() {
		clear_tree(root);
		length = 0;
	};
	const iterator* find(T element) {
		if (root != nullptr) {
			if (element < (*(root)).get()) {
				search(element, root->left_element);
			}
			else if (element >= (*(root)).get()) {
				search(element, root->right_element);
			}
		}
		else
			return nullptr;
	};
	
	// Checks if element is a part of the tree
	bool isElement(const T& element) {
		return find(element) != nullptr;
	}

	// Insert new element into the tree
	void insert(const T& element) {
		if (root != nullptr) {
			insert(element, root);
		}
		else {
			root = new iterator;
			root->left_element = nullptr;
			root->right_element = nullptr;
			((*root).get()) = element;
			root->parent = nullptr;
			++length;
		}
	};
	void remove(T element) {
		auto it = find(element);
		remove(it);
	};
	void remove(iterator* node) {
		if (node != nullptr) {
			auto it_p = node->parent;
			auto right = node->right_element;
			if (right != nullptr) {
				auto it = far_end(1, right);
				it->left_element = new iterator;
				it->left_element = node->left_element;
				node->left_element->parent = it;
				it_p->right_element = right;
				right->parent = it_p;
			}
			else {
				it_p->left_element = node->left_element;
				node->left_element->parent = it_p;
			}

			delete node;
			--length;
		}
	}
	int size() {
		return length;
	};
	
	// Next left element
	const iterator* successor_min(iterator* node) {
		return node->left_element;
	};
	
	// Next right element
	const iterator* successor_max(iterator* node) {
		return node->right_element;
	};
	
	const iterator* previous(iterator* node) {
		return node->parent;
	};
	const iterator* end() {
		return nullptr;
	};
	const iterator* begin() {
		return root;
	};
	
	/*
	* Output tree into a console
	*/
	void Write() {
		if (root != nullptr) {
			std::cout << "{\t" << (*(root)).get() << ": \n\t\t{";
			write(root->left_element);
			std::cout << "}, \n\t\t{";
			write(root->right_element);
			std::cout << "};\n};\n";
		}
		else
			std::cout << "Tree is empty\n";
	};
	T& operator[](iterator it) {
		return it.get();
	}
	
	// Maximal element of the tree(far end)
	T& max() {
		iterator* it = nullptr;
		if (root != nullptr) {
			if (root->right_element != nullptr) {
				it = far_end(0, root->right_element);
			}
			else
				it = root;
		}
		return (*it).get();
	};

	// Minimal element of the tree(begining)
	T& min() {
		iterator* it = nullptr;
		if (root != nullptr) {
			if (root->left_element != nullptr) {
				it = far_end(1, root->left_element);
			}
			else
				it = root;
		}
		return (*it).get();
	};
	bool isEmpty() {
		return (root == nullptr);
	}
private:
	class iterator {
	public:
		iterator & operator=(const iterator& IT) {
			data = IT.get();
			(*this)->left_element = IT->left_element;
			(*this)->right_element = IT->rigth_element;
			return *this;
		};
		bool operator==(const iterator& it) {
			bool flag1, flag2, flag3;
			flag1 = (data == IT.get());
			flag2 = ((*this)->left_element == IT->left_element);
			flag3 = ((*this)->right_element == IT->rigth_element);
			return flag1 && flag2 && flag3;
		};
		bool operator!=(const iterator& it) {
			return !(*this == it);
		};
		T& get() {
			return data;
		};
		const T& cget() const {
			return data;
		}
		iterator* left_element;
		iterator* right_element;
		iterator* parent;
	private:
		T data;
	};
	iterator *root;
	int length;
	void clear_tree(iterator* leaf) {
		if (leaf != nullptr) {
			clear_tree(leaf->left_element);
			clear_tree(leaf->right_element);
			delete leaf;
		}
	};
	void insert(T value, iterator* leaf) {
		if (value < (*leaf).get()) {
			if (leaf->left_element != nullptr) {
				insert(value, leaf->left_element);
			}
			else {
				leaf->left_element = new iterator;
				(*(leaf->left_element)).get() = value;
				leaf->left_element->left_element = nullptr;
				leaf->left_element->right_element = nullptr;
				leaf->left_element->parent = leaf;
				++length;
			}
		}
		else if (value > (*leaf).get()) {
			if (leaf->right_element != nullptr) {
				insert(value, leaf->right_element);
			}
			else {
				leaf->right_element = new iterator;
				(*(leaf->right_element)).get() = value;
				leaf->right_element->left_element = nullptr;
				leaf->right_element->right_element = nullptr;
				leaf->right_element->parent = leaf;
				++length;
			}
		}
		else
			return;
	}
	iterator* search(T value, iterator* leaf) {
		if (leaf != nullptr) {
			if (value == (*(leaf)).cget()) {
				return leaf;
			}
			else if (value < (*(leaf)).cget()) {
				return search(value, leaf->left_element);
			}
			else if (value >(*(leaf)).cget()) {
				return search(value, leaf->right_element);
			}
		}
		else return end();
	}
	void write(iterator* leaf) {
		if (leaf != nullptr) {
			std::cout << (*leaf).cget() << ": {";
			write(leaf->left_element);
			std::cout << "}, {";
			write(leaf->right_element);
			std::cout << "};";
		}
		else
			return;
	}
	iterator* far_end(bool left, iterator* leaf) {
		if (left) {
			if (leaf->left_element != nullptr)
				return far_end(left, leaf->left_element);
			else return leaf;
		}
		else {
			if (leaf->right_element != nullptr)
				return far_end(left, leaf->right_element);
			else return leaf;
		}
	}
};