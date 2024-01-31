# encoding: utf-8

from waflib import Configure, Logs

def options(opt):
	grp = opt.add_option_group('CCache')

	grp.add_option('--ccache', action = 'store_true', dest = 'CCACHE', default = False,
		help = 'Build with CCache. [default: %default]')

def configure(conf):
	if conf.options.CCACHE:
		conf.find_program('ccache')
		Logs.info('INFO: will build with CCache')
		conf.env.CC  = ''.join(conf.env.CCACHE), ''.join(conf.env.CC)
		conf.env.CXX = ''.join(conf.env.CCACHE), ''.join(conf.env.CXX)
