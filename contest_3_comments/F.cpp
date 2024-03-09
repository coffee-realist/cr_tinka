#include <iostream>
#include <cstdlib>
#include <ctime>
#include <climits>

class TreapNode {
public:
    int key;
    int priority;
    TreapNode *left, *right;

    TreapNode(int key) : key(key), left(nullptr), right(nullptr) {
        priority = rand() % (UINT64_MAX) + 1;
    }
};

TreapNode* right_rotate(TreapNode* v) {
    TreapNode* v_left = v->left;
    TreapNode* v_left_right = v_left->right;
    v_left->right = v;
    v->left = v_left_right;
    return v_left;
}

TreapNode* left_rotate(TreapNode* v) {
    TreapNode* v_right = v->right;
    TreapNode* v_right_left = v_right->left;
    v_right->left = v;
    v->right = v_right_left;
    return v_right;
}

TreapNode* add(TreapNode* root, int key) {
    if (!root) {
        return new TreapNode(key);
    }
    if (root->key >= key) {
        root->left = add(root->left, key);
        if (root->priority < root->left->priority) {
            root = right_rotate(root);
        }
    } else {
        root->right = add(root->right, key);
        if (root->priority < root->right->priority) {
            root = left_rotate(root);
        }
    }
    return root;
}

std::pair<TreapNode*, int> _next(TreapNode* root, int key, int min_ans) {
    if (!root || root->key == key) {
        return {root, min_ans};
    }
    if (root->key < key) {
        return _next(root->right, key, min_ans);
    }
    return _next(root->left, key, root->key < min_ans ? root->key : min_ans);
}

int main() {
    srand(0);
    TreapNode* treap = nullptr;
    int q;
    std::cin >> q;
    char last_op = '+';
    int last_ans = 0;
    const int m = 1000000000;
    for (int i = 0; i < q; ++i) {
        char op;
        int n;
        std::cin >> op >> n;
        if (op == '+') {
            if (last_op == '+') {
                treap = add(treap, n);
            } else {
                treap = add(treap, (n + last_ans) % m);
            }
        } else {
            auto [r, ans] = _next(treap, n, INT_MAX);
            last_ans = r ? r->key : ans;
            if (last_ans < n || last_ans == INT_MAX) {
                last_ans = -1;
            }
            std::cout << last_ans << std::endl;
        }
        last_op = op;
    }
    return 0;
}
