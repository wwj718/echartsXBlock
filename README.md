#echartsXBLock by wwj718<wuwenjie718@gmail.com>
This package provides an XBlock to use [echarts](https://github.com/ecomfe/echarts) in edX platform

echart demo : <http://echarts.baidu.com/doc/example.html>



#Installation
*  sudo su edxapp -s /bin/bash
*  cd ~
*  source edxapp_env
*  pip install -e git+https://github.com/wwj718/echartsXBLock
*  in /edx/app/edxapp/cms.envs.json add `"ALLOW_ALL_ADVANCED_COMPONENTS": true,` to  to the list of FEATURES

#Course Authoring in edX Studio
1.  Change Advanced Settings
    *  Open a course you are authoring and select "Settings" ⇒ "Advanced Settings
    *  Navigate to the section titled "Advanced Module List"
    *  Add "echart" to module list

2.  Create an echart XBlock
    *  Return to the Course Outline
    *  Create a Section, Sub-section and Unit, if you haven't already
    *  In the "Add New Component" interface, you should now see an "Advanced" button
    *  Click "Advanced" and choose "echart"

#echart
![echarts1](http://7sby7q.com1.z0.glb.clouddn.com/echarts1.jpeg)
![echarts2](http://7sby7q.com1.z0.glb.clouddn.com/echarts2.jpeg)
![echarts3](http://7sby7q.com1.z0.glb.clouddn.com/echarts3.jpeg)
![echarts4](http://7sby7q.com1.z0.glb.clouddn.com/echarts4.jpeg)
![echarts5](http://7sby7q.com1.z0.glb.clouddn.com/echarts5.jpeg)
