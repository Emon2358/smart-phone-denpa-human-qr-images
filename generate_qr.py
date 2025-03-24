import os
import random
import string
import qrcode

# 生成するQRコードの総数（1〜99999個）
NUM_QR = 99999

def random_string(length=10):
    """ランダムな英数字の文字列を生成する"""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def generate_qr_codes(num):
    """QRコードを生成してqrフォルダに保存する"""
    for i in range(1, num + 1):
        # 固定の "https://" に続いてランダムな文字列を付与
        data = "https://" + random_string(10)
        # QRコードを生成
        img = qrcode.make(data)
        # わかりやすいようにゼロパディングしたファイル名で保存
        filename = os.path.join("qr", f"qr_{i:05d}.png")
        img.save(filename)
        # 進捗表示（1000枚ごと）
        if i % 1000 == 0:
            print(f"{i} QR codes generated.")

if __name__ == "__main__":
    generate_qr_codes(NUM_QR)
