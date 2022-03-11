// задание 1  задача 7 Найти минимальный элемент исходного стека и создать новый стек, 
// путем умножения элементов исходного стека на найденный 
// минимальный элемен

#include <iostream>
#include <stack>								// добавляем библиотеку для стека

using namespace std;

int main() {
	stack <int> first_stack;						// объявляем стек
	int enter_number;

	while (true)									// пока цикл while true заполняем стек
	{
		cout << "enter -99 to exit or enter number to add for stack: ";   // тут наверное все понятно
		cin >> enter_number;						// добавляем новые элементы для стека, добавляет пользователь
		if (enter_number == -99) break;				// если enter_number ровно -99 выходим из цикла
		cout << endl;
		first_stack.push(enter_number);				// заполняем стек новыми элементами

	}

	cout << "First stack size: " << first_stack.size();		// выводим размер стека
	enter_number = size(first_stack);
	int min_num = first_stack.top();						// минимальная число пока равен самому первому элементу стека
	cout << min_num << endl;
	for (int i = 0; i < enter_number; i++) {			// цикл (ну я не знаю что писать просто объявил цикл)
		if (min_num > first_stack.top()) {					// есди минимальная число больше элемента стека тут написано
			min_num = first_stack.top();					// минимальный элемент равно на элемент стека
		}
		cout << min_num<<endl;
		first_stack.pop();									// удаляем элемент стека что бы получить другие элементы стека по очереди
	}
	cout << endl;
	cout << "Minimum number in first stack: " << min_num << endl;	// тут типа показываем минимальную элемент

	cout << "ente size stack: " << endl;
	stack <int> new_stack;									// создаем новый стек
	int size_stack, rand_num;
	cin >> size_stack;										// даем размер новому стеку


	for (int i = 0; i < size_stack; i++) {				// в этом цикле заполняем новый стек рандомными элементами
		rand_num = 1 + rand() % 100;
		cout << "random numbers to fit new stack: " << rand_num << endl;	// выводим рандомные числа
		new_stack.push(rand_num * min_num);								// заполняем стек фомулой рандомные числа * минимальная число предедущего стека
	}
	cout << "New stack size: " << new_stack.size() << endl;

	cout << "New stack elements: " << endl;
	for (int i = 0; i < size_stack; i++) {			// выводим и удаляем элементы стека
		cout << new_stack.top() << endl;
		new_stack.pop();
	}
}