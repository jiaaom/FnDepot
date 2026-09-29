# Appliance Compositor

[English](README.md) | 简体中文

fnOS 上屏幕类应用共用的显示和声音服务：一个 Wayland 合成器（weston + appliance-shell）驱动所有屏幕，一个 PipeWire 声音服务。它本身没有窗口；T6 前面板、Fygo Cinema 等应用作为它的窗口，各自显示在对应的屏幕上。

源码：<https://github.com/jiaaom/appliance-compositor>

## 安装

请在依赖它的应用（T6 前面板、Fygo Cinema）**之前**安装。

- 缺少时会从 Debian bookworm-backports 自动安装 weston 14、Mesa 24 和 PipeWire。
- 系统中装有 PulseAudio 时会拒绝安装。
- 仍有应用在使用它时，无法卸载。

## 问题反馈

<https://github.com/jiaaom/appliance-compositor/issues>
