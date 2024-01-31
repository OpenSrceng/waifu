# encoding: utf-8

from waflib import Configure, Logs
import os.path

@Configure.conf
def check_32bit(ctx, *k, **kw):
	if not 'msg' in kw:
		kw['msg'] = 'Checking if \'%s\' can target 32-bit' % ctx.env.COMPILER_CC

	if not 'mandatory' in kw:
		kw['mandatory'] = False

	return ctx.check_cc( fragment='int main(void){int check[sizeof(void*)==4?1:-1];return 0;}', *k, **kw)

def options(opt):
	grp = opt.add_option_group('Android NDK')

	grp.add_option('--ndk', action = 'store_true', dest = 'NDK', default = False,
		help = 'Build with android ndk. [default: %default]')

	grp.add_option('--ndk-path', action = 'store', dest = 'NDK_PATH', default = '/ndk/path/toolchains/llvm/prebuilt/linux-x86_64/bin',
		help = 'Set path to android ndk. [default: %default]')

def configure(conf):
	if conf.options.NDK:
		Logs.info('INFO: will build for android ndk')

		if conf.check_32bit():
			Logs.error('ERROR: didn\'t support 32bits for android ndk')

		ndk_toolchain_path = os.path.abspath(conf.options.NDK_PATH)

		if conf.env.DEST_OS != 'linux':
			Logs.error('ERROR: NDK only support linux so implete me')

		# Android API 28 ( Android 9 ) ( support iconv and vulkan1.1 )
		conf.env.CC				= ndk_toolchain_path + '/toolchains/llvm/prebuilt/linux-x86_64/bin/aarch64-linux-android28-clang'
		conf.env.CXX			= ndk_toolchain_path + '/toolchains/llvm/prebuilt/linux-x86_64/bin/aarch64-linux-android28-clang++'
		conf.env.AR				= ndk_toolchain_path + '/toolchains/llvm/prebuilt/linux-x86_64/bin/llvm-ar'
		conf.env.STRIP			= ndk_toolchain_path + '/toolchains/llvm/prebuilt/linux-x86_64/bin/llvm-strip'
		conf.env.COMPILER_CC	= 'clang'
		conf.env.DEST_OS		= 'android'
		conf.env.DEST_CPU		= 'aarch64'
		conf.env.DEST_FMT		= 'elf'
		conf.env.append_unique('LINKFLAGS', ['-static-libstdc++'])

		if conf.check_32bit():
			Logs.error('ERROR: didn\'t support 32bits for android ndk')
