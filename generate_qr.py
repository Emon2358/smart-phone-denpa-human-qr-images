import os
import random
import string
import qrcode

# 生成するQRコードの総数（ここでは10個）
NUM_QR = 10

def random_string(length=153):
    """ランダムな英数字の文字列を生成する"""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def generate_qr_codes(num):
    """QRコードを生成してqrフォルダに保存する"""
    for i in range(1, num + 1):
        # Chrome の恐竜ゲームを起動するコードにランダムなクエリ文字列を追加
        data = "chrome://dino?" + random_string(153)
        # QRコードを生成
        img = qrcode.make(data)
        # わかりやすいようにゼロパディングしたファイル名で保存
        filename = os.path.join("qr", f"qr_{i:05d}.png")
        img.save(filename)
        print(f"QR code {i} generated.")

if __name__ == "__main__":
    generate_qr_codes(NUM_QR)
