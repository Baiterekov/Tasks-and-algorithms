/* задание 3  задача 7 Название фирмы, название услуги, 
продолжительность выполнения, цена
Определить среднее цену по всем видам 
услуг, затем выведите все фирмы, цена 
услуги которых ниже среднего значения.*/


#include <iostream>

using namespace std;

struct business {
	string company_name;
	string service_name;
	string duration_of_execution;
	float cost;
};

int main() {
	business company1 = { "first company", "service 1", "5 sec", 5.00 };
	business company2 = { "second company", "service 1", "10 sec", 10.00 };
	business company3 = { "third company", "service 1", "6 sec", 6.00 };
	business company4 = { "forth company", "service 1", "8 sec", 8.00 };
	business company5 = { "fifth company", "service 1", "12 sec", 12.00 };
	business company6 = { "sixth company", "service 1", "9 sec", 9.00 };
	business company7 = { "seventh company", "service 1", "15 sec", 15.00 };
	business company8 = { "eighth company", "service 1", "4 sec", 4.00 };

	float average_cost = (company1.cost + company2.cost + company3.cost + company4.cost + company5.cost + company6.cost + company7.cost + company8.cost) / 8;

	cout << "Average cost: " << average_cost << endl;
	cout << endl;

	if (average_cost > company1.cost) {
		cout << company1.company_name << " " << company1.cost << "$ " << company1.service_name << " " << company1.duration_of_execution << endl;
	}
	if (average_cost > company2.cost) {
		cout << company2.company_name << " " << company2.cost << "$ " << company2.service_name << " " << company2.duration_of_execution << endl;
	}
	if (average_cost > company3.cost) {
		cout << company3.company_name << " " << company3.cost << "$ " << company3.service_name << " " << company3.duration_of_execution << endl;
	}
	if (average_cost > company4.cost) {
		cout << company4.company_name << " " << company4.cost << "$ " << company4.service_name << " " << company4.duration_of_execution << endl;
	}
	if (average_cost > company5.cost) {
		cout << company5.company_name << " " << company5.cost << "$ " << company5.service_name << " " << company5.duration_of_execution << endl;
	}
	if (average_cost > company6.cost) {
		cout << company6.company_name << " " << company6.cost << "$ " << company6.service_name << " " << company6.duration_of_execution << endl;
	}
	if (average_cost > company7.cost) {
		cout << company7.company_name << " " << company7.cost << "$ " << company7.service_name << " " << company7.duration_of_execution << endl;
	}
	if (average_cost > company8.cost) {
		cout << company8.company_name << " " << company8.cost << "$ " << company8.service_name << " " << company8.duration_of_execution << endl;
	}

	system("pause");
	return 0;
}
