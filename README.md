# Devicer

---

Linux输入设备活动监视器

---

## 运行环境

- Linux
- `python --version` >= 3.6

## 依赖

- [evdev](<https://github.com/gvalkov/python-evdev>)

## 安装方法

```shell
# 在'Devicer'文件夹（setup.py同一路径）下
pip install .
```

> **注意：**
>
> 1. 不要遗漏最后的 **`.`**
> 2. `pip --version` >= 3.6

## 可用命令

```shell
# findevices

> device path  |  device name  |  device type
> /dev/input/event16  |  HDA Intel PCH HDMI/DP,pcm=10  |  ALSA
> ...
> /dev/input/event0  |  Power Button  |  PNP0C0C/button/input0
```

