# Orion
Orion is a xxx

## Getting Started
### Installation
```
pip install git+https://github.com/username/repo-name.git
```

### Adopting Devices on Network
Orion is capable of automatically adopting devices already present on home assistant by running orion with the ```--adopt``` argument as shown below
```
orion --adopt
```

## Rest API
Orion automatically creates 3 endpoints for each adopted device, allowing anyone on the network to either toggle the device or turn it on/off. For example, below are the endpoints that would be registered for a device called ```Lamp1```

```
<Server IP>/device/Lamp1/on
<Server IP>/device/Lamp1/off
<Server IP>/device/Lamp1/toggle
```

Additionally, similar points are generated for groups that are created using Orion (More on groups below). Below is an example of the endpoints generated for a group called ```Office```. 

```
<Server IP>/group/Office/on
<Server IP>/group/Office/off
<Server IP>/group/Office/toggle
```

## Utilizing Groups and Devices
Orion allows you to easily create trigger groups for different devices present on your network by putting them all under 1 endpoint. These groups can become very usefull as implementing them with custom IOT hardware allows you to easily reconfigure how the IOT device interacts with your home without having to reflash firmware to said device.


### Managing Groups
Creating and managing groups using arguments is very simple and straightforward as shown below. Please note that in order for a device to be added to a group, it has to be adopted. If your device does not appear after using ```--adopt```, you can manually add the device as shown in the next section. 

#### Creating Group
```
orion --createGroup --groupName <Group Name>
```
#### Deleting Group
```
orion --removeGroup --groupName <Group Name>
```
#### Adding Device to Group
```
orion --addDeviceToGroup --groupName <Group Name> --deviceName <Device Name>
```
#### Removing Device from Group
```
orion --removeDeviceFromGroup --groupName <Group Name> --deviceName <Device Name>
```

### Managing Devices
#### Adding Device
```
orion --addDevice --deviceName <Device Name>
```
#### Removing Device
```
orion --removeDevice --deviceName <Device Name>
```

## Orion Framework

Orion Framework is an arduino framework library that allows you to easily make calls to an Orion instance using WiFi capable microcontrollers such as the ESP32. 