# FygoOS/fnOS App Repo

English | [简体中文](README.zh-CN.md)

An app source for [FnDepot](https://github.com/EWEDLCM/FnDepot), the third-party app store for fnOS.

## Add this source

In the [FnDepot](https://github.com/EWEDLCM/FnDepot) client, add:

```
https://github.com/jiaaom/FnDepot
```

## Apps

| Icon | App | Description | Source |
| :---: | --- | --- | --- |
| <img src="t6-drivers/ICON.PNG" width="48" alt="t6-drivers"> | [T6 Drivers](t6/README.md)<br>`t6-drivers` | Kernel drivers for the UnifyDrive UP6 / ZSpace T6: fans, LEDs, backlight, battery, touchscreen and more. Install first. | [up6-linux-drivers](https://github.com/jiaaom/up6-linux-drivers) |
| <img src="t6-control/ICON.PNG" width="48" alt="t6-control"> | [T6 Control Center](t6/README.md)<br>`t6-control` | Fan curves, LEDs, brightness, battery charge limit and beeper settings. Requires T6 Drivers. | [up6-linux-drivers](https://github.com/jiaaom/up6-linux-drivers) |
| <img src="appliance-compositor/ICON.PNG" width="48" alt="appliance-compositor"> | [Appliance Compositor](appliance-compositor/README.md)<br>`appliance-compositor` | Shared display and sound server for screen apps (weston + PipeWire), with no window of its own. Install it before T6 Front Panel and Fygo Cinema. | [appliance-compositor](https://github.com/jiaaom/appliance-compositor) |
| <img src="t6-panel/ICON.PNG" width="48" alt="t6-panel"> | [T6 Front Panel](t6/README.md)<br>`t6-panel` | Front touch-screen app: overview, files, network and device settings, and a built-in video/music player. Requires T6 Control Center and Appliance Compositor. | [up6-linux-drivers](https://github.com/jiaaom/up6-linux-drivers) |
| <img src="fygo-cinema/ICON.PNG" width="48" alt="fygo-cinema"> | [Fygo Cinema](fygo-cinema/README.md)<br>`fygo-cinema` | Fygo TV on your TV with a remote: hardware decoding, signs in by itself, starts when the TV is plugged in. Requires Fygo TV and Appliance Compositor. | [fygo-cinema](https://github.com/jiaaom/fygo-cinema) |

Each app links to its own source code and issue tracker.
