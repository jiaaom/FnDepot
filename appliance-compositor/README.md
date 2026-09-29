# Appliance Compositor

English | [简体中文](README.zh-CN.md)

The shared display and sound server for screen apps on fnOS: one Wayland
compositor (weston + appliance-shell) on every display, and one PipeWire sound
server. It has no window of its own. Apps such as T6 Front Panel and Fygo
Cinema appear as its windows, each on the display it belongs to.

Source: <https://github.com/jiaaom/appliance-compositor>

## Install

Install it **before** the apps that use it (T6 Front Panel, Fygo Cinema).

- It installs weston 14, Mesa 24 and PipeWire from Debian bookworm-backports
  when they are missing.
- It refuses to install while PulseAudio is present.
- Uninstalling is refused while apps still use it.

## Issues

<https://github.com/jiaaom/appliance-compositor/issues>
