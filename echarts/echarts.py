#coding=utf-8
#author: wwj718
#author_email: wuwenjie718@gmail.com
#author_blog: wwj718.github.io

""" echartsXBlock main Python class"""

import pkg_resources
from django.template import Context, Template

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String, Boolean
from xblock.fragment import Fragment

import logging
logger = logging.getLogger(__name__)
LOG_FILE = "/home/wwj/xblock/echartsXBlock/echarts/log_text.log"
handler=logging.FileHandler(LOG_FILE)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

LOG_FILE = "log_file.log"
class echartsXBlock(XBlock):

    '''
    Icon of the XBlock. Values : [other (default), video, problem]
    '''
    icon_class = "video"

    '''
    Fields
    '''
    display_name = String(display_name="Display Name",
        default="echarts player",
        scope=Scope.settings,
        help="This name appears in the horizontal navigation at the top of the page.")

    echarts_data = String(display_name=" echarts_data",
	default="echarts_data",
	scope=Scope.settings, #粒度最小
	help="The echarts_data for your echarts.")



    app_id = String(display_name="video client_id",
	default="echarts",
	scope=Scope.content, #Scope.content和Scope.settings不同在于，(可见性)本课多处可用
	help="The  client_id for your video.")

    file_id = String(display_name="video vid",
	default="echarts",
	scope=Scope.content, #Scope.content和Scope.settings不同在于，(可见性)本课多处可用
	help="The vid for your video.")


    width = Integer(display_name="Video player width",
	default="560",
	scope=Scope.content,
	help="The width for your video player.")
    height = Integer(display_name="Video player height",
	default="320",
	scope=Scope.content,
	help="The height for your video player.")

    '''
    Util functions
    '''
    def load_resource(self, resource_path):
        """
        Gets the content of a resource
        """
        resource_content = pkg_resources.resource_string(__name__, resource_path)
        return unicode(resource_content)

    def render_template(self, template_path, context={}):
        """
        Evaluate a template by resource path, applying the provided context
        """
        template_str = self.load_resource(template_path)
        return Template(template_str).render(Context(context))

    '''
    Main functions
    '''
    def student_view(self, context=None):
        """
        The primary view of the XBlock, shown to students
        when viewing courses.
        """
        '''
	    #添加字段记录上回播放时间，应该是用户级别的
	    if self.start_time != "" and self.end_time != "":
            fullUrl += "#t=" + self.start_time + "," + self.end_time
        elif self.start_time != "":
            fullUrl += "#t=" + self.start_time
        elif self.end_time != "":
            fullUrl += "#t=0," + self.end_time
        '''
        context = {
            'display_name': self.display_name,
            'echarts_data': self.echarts_data
        }
        html = self.render_template('static/html/echarts_view.html', context)
        frag = Fragment(html)
        frag.add_javascript_url("http://echarts.baidu.com/doc/asset/css/codemirror.css")
        frag.add_javascript_url("http://echarts.baidu.com/doc/asset/js/codemirror.js")
        frag.add_javascript_url("http://echarts.baidu.com/build/dist/echarts-all.js")
        frag.add_javascript(self.load_resource("static/js/macarons.js"))
        frag.add_javascript(self.load_resource("static/js/echarts_view.js"))
        frag.initialize_js('echartsXBlockInitView')
        return frag

    def studio_view(self, context=None):
        """
        The secondary view of the XBlock, shown to teachers
        when editing the XBlock.
        """
        context = {
            'display_name': self.display_name,
            'echarts_data': self.echarts_data
        }
        html = self.render_template('static/html/echarts_edit.html', context)
        frag = Fragment(html)
        frag.add_javascript_url("http://echarts.baidu.com/doc/asset/css/codemirror.css")
        frag.add_javascript_url("http://echarts.baidu.com/doc/asset/js/codemirror.js")
        frag.add_javascript_url("http://echarts.baidu.com/build/dist/echarts-all.js")
        frag.add_javascript(self.load_resource("static/js/macarons.js"))
        frag.add_javascript(self.load_resource("static/js/echarts_edit.js"))
        frag.initialize_js('echartsXBlockInitStudio')
        logger.info("studio_view|return")
        return frag

    @XBlock.json_handler
    def save_echarts(self, data, suffix=''):
        """
        The saving handler.
        """
        self.display_name = data['display_name']
        self.echarts_data= data['echarts_data']

        return {
            'result': 'success',
        }

    @XBlock.json_handler
    def get_params(self, data, suffix=''):
        '''called when echarts init'''
        return {"file_id":self.file_id,
                "app_id":self.app_id,
                "width":self.width,
                "height":self.height
                }

    @staticmethod
    def workbench_scenarios():
        return [
              ("echarts demo", "<echarts />")  #the name should be "<echarts />"
        ]
