
import sys

user_input_cpf = input('CPF: ') \
    .replace('.', '') \
    .replace(' ', '') \
    .replace('-', '') 

is_sequential_input = user_input_cpf == user_input_cpf[0] * len(user_input_cpf)

if is_sequential_input:
    print('You entered sequential data')
    sys.exit()

nine_digits = user_input_cpf[:9]
countdown_counter_1 = 10

result_digit_1 = 0
for digit in nine_digits:
    result_digit_1 += int(digit) * countdown_counter_1
    countdown_counter_1 -= 1

digit_1 = (result_digit_1 * 10) % 11
digit_1 = digit_1 if digit_1 <= 9 else 0

ten_digits = nine_digits + str(digit_1)
countdown_counter_2 = 11

result_digit_2 = 0
for digit in ten_digits:
    result_digit_2 += (int(digit) * countdown_counter_2)
    countdown_counter_2 -= 1

digit_2 = (result_digit_2 * 10) % 11
digit_2 = digit_2 if digit_2 <= 9 else 0

calculated_cpf = f'{nine_digits}{digit_1}{digit_2}'

if user_input_cpf == calculated_cpf:
    print(f'{user_input_cpf} is valid')
else:
    print('Invalid CPF')
