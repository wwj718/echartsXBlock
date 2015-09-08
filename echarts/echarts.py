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

'''
logger = logging.getLogger(__name__)
LOG_FILE = "/home/wwj/xblock/echartsXBlock/echarts/log_text.log"
handler=logging.FileHandler(LOG_FILE)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
'''

class echartsXBlock(XBlock):

    '''
    Icon of the XBlock. Values : [other (default), video, problem]
    '''
    icon_class = "other"

    '''
    Fields
    '''
    display_name = String(display_name="Display Name",
        default="echarts",
        scope=Scope.settings,
        help="This name appears in the horizontal navigation at the top of the page.")

    echarts_data = String(display_name=" echarts_data",
	default="echarts_data",
	scope=Scope.settings,
	help="The echarts_data for your echarts.")


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
        #logger.info("studio_view|return")
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

    @staticmethod
    def workbench_scenarios():
        return [
              ("echarts demo", "<echarts />")  #the name should be "<echarts />"
        ]
