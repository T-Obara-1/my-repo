# import subprocess
# import os
# 以下は Bandit によって検出される可能性のあるセキュリティ上の問題を含むコード例です。

# def insecure_eval(user_input):
#     # B101: 使用すべきでない eval 関数
#     return eval(user_input)
# 
# def hardcoded_password():
#     # B105: ハードコーディングされたパスワード
#     password = "SuperSecret123"
#     print("Password is:", password)
# 
# def dangerous_subprocess():
#     # B603: subprocess の shell=True は危険
#     command = "ls -la"
#     subprocess.call(command, shell=True)
# 
# def weak_random():
#     # B311: セキュリティ用途に不適切な乱数生成
#     import random
#     token = random.random()
#     print("Token:", token)
# 
# def insecure_temp_file():
#     # B108: 安全でない一時ファイルの作成
#     f = open("/tmp/mytempfile.txt", "w")
#     f.write("Sensitive data")
#     f.close()
