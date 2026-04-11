//C++ Hello World Child prosecc
#include <iostream>

using namespace std;

char Vinput[] = "Invalid input";
char line[] = "-------------------------";

int main() {

    while (1) {
        cout << line << endl;
        cout << "Hello World!" << endl;
        cout << line << endl;
        cout << "Type 'Q' to quit" << endl;
        cout << "> ";

        string choice;
        cin >> choice;

        if (choice == "Q") {
            break;
        } else {
            cout << Vinput << endl;
        }
    }
    return 0;
}