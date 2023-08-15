import requests
import json

# 바이낸스 API 엔드포인트
url = 'https://fapi.binance.com/fapi/v1/klines'

# 조회할 선물 심볼
symbol = 'BTCUSDT'

# 조회할 캔들 시간 간격 (1분)
interval = '1m'

# 조회할 캔들 수
limit = 10

# API 호출에 필요한 매개변수 설정
params = {
    'symbol': symbol,
    'interval': interval,
    'limit': limit
}

# API 호출 및 데이터 분석
response = requests.get(url, params=params)
data = json.loads(response.text)

for candle in data:
    print('시간:', candle[0])
    print('시가:', candle[1])
    print('고가:', candle[2])
    print('저가:', candle[3])
    print('종가:', candle[4])
    print('거래량:', candle[5])