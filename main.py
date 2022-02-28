from api.Kiwoom import *
import sys
from strategy.RSIStrategy import *

app = QApplication(sys.argv)

rsi_strategy = RSIStrategy()
rsi_strategy.start()

app.exec_()

# # 1~7 까지 주석을 테스트할 경우 공통으로 사용
# app = QApplication(sys.argv)
# kiwoom = Kiwoom()

# 7. 실시간 정보 조회
# # kiwoom.set_real_reg("1000", "", get_fid("장운영구분"), "0")
# fids = get_fid("체결시간")
# codes = '005930;007700;006600;'
# kiwoom.set_real_reg("1000", codes, fids, "0")
#
# app.exec_()

# # 6. 게좌잔고조회
# position = kiwoom.get_balance()
# print(position)
# app.exec_()

# 5. 체결조회
# orders = kiwoom.get_order()
# print(orders)
# app.exec_()

# # 4. 매수주문
#
# order_result = kiwoom.send_order('send_buy_order', '1001', 1, '007700', 1, 27200, '00')
#
# print(order_result)
#
# app.exec_()

# # 3. 예수금정보 가져오기 (결과나오지않음)
# deposit = kiwoom.get_deposit()
# app.exec_()

# 2. 종목정보 가져오기 - 삼성전자
# df = kiwoom.get_price_data("005930")
# print(df)
# 
# app.exec_()

# 1. 종목 목록 가져오기
# # 종목리스트 0:코스피, 10:코스닥
# kospi_code_list = kiwoom.get_code_list_by_market("0")
# print(kospi_code_list)
# # 종목명 리스트
# for code in kospi_code_list:
#     code_name = kiwoom.get_master_code_name(code)
#     print(code, code_name)
#
# kosdaq_code_list = kiwoom.get_code_list_by_market("10")
# print(kosdaq_code_list)
# # 종목명 리스트
# for code in kosdaq_code_list:
#     code_name = kiwoom.get_master_code_name(code)
#     print(code, code_name)
# app.exec_()
