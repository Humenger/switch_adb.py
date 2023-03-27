# -*- coding: utf-8 -*-
import os
import time

# ��ȡ��ǰANDROID_SERIAL��������
current_device = os.environ.get("ANDROID_SERIAL")

# �г������ӵ�Android�豸�б�
devices = []
models = []
for line in os.popen("adb devices").readlines():
    if "List of devices attached" not in line and line.strip() != "":
        device_id = line.split("\t")[0]
        devices.append(device_id)

# ����豸�Ƿ�������һ��
if len(devices) == 0:
    print("No devices found.")
    exit()

# ��ʾ�����豸�б������豸�ͺź�Android�汾��
print("{:<8}{:<30}{:<16}{}".format("Index", "Device ID", "Model", "Version"))
for index, device_id in enumerate(devices):
    model = os.popen(f"adb -s {device_id} shell getprop ro.product.model").read().strip()
    android_version = os.popen(f"adb -s {device_id} shell getprop ro.build.version.release").read().strip()
    models.append(model)
    print("{:<8}{:<30}{:<16}{}".format(f"[{index + 1}]", device_id, model, android_version))

# �����û�ѡ��Ҫ���ӵ��豸
choice = input("Enter device number to switch to: ")

# �л���ѡ����豸
try:
    choice = int(choice) - 1
    device_id = devices[choice]
    os.environ["ANDROID_SERIAL"] = device_id
    os.system("setx \"ANDROID_SERIAL\" \"%s\""%device_id)
    #os.system("set ANDROID_SERIAL=%s&&start cmd /k \"adb shell\""%device_id)
    print("\n[OK] Already switch to ",device_id)
    #os.environ["ANDROID_SERIAL"] = current_device
except (ValueError, IndexError):
    print("Invalid choice.")
time.sleep(3)
