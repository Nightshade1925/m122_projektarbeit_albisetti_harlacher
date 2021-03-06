import os
import json
import logging
import logging.handlers


class Utils:

	@staticmethod
	def register_handlers(file_log_level, log_path) -> None:
		"""
		Register all log handlers

		Register a file handler for the application as a default logger with settings form the configuration\
		Register a console handler. Default loglevel is INFO.

		:return:
		"""
		# Set root Log Level to DEBUG so that all logs are passed to the handlers
		logging.getLogger().setLevel('DEBUG')
		# Create File handler
		# File handler logs on configured log level to file
		file_handler = Utils.register_file_handler(file_log_level=file_log_level, log_path=log_path)
		logging.getLogger().addHandler(file_handler)

		# Create Console Handler
		# Console handler logs on INFO as default
		console_handler = Utils.register_console_handler()
		logging.getLogger().addHandler(console_handler)

	@staticmethod
	def register_file_handler(log_path, file_log_level) -> logging.FileHandler:
		formatter = logging.Formatter('{asctime} {name} {levelname:8s} {message}', style='{')
		handler = logging.handlers.RotatingFileHandler(filename=log_path,
													   backupCount=15,
													   maxBytes=10000)  # 10kb
		handler.setFormatter(formatter)
		handler.setLevel(file_log_level)
		return handler

	@staticmethod
	def register_console_handler() -> logging.StreamHandler:
		handler = logging.StreamHandler()
		handler.setLevel("INFO")
		return handler

	@staticmethod
	def enable_debug_flag() -> None:
		for handler in logging.getLogger().handlers:
			handler.setLevel("DEBUG")

	@staticmethod
	def load_config() -> dict:
		"""
		Loads the configuration file and returns a dictionary with the configuration
		:return:
		"""
		dirname = os.path.dirname(__file__)
		filename = os.path.join(dirname, '../etc/config.json')
		try:
			c = open(filename, 'r')
			config = json.load(c)
			c.close()
			return config
		except Exception as e:
			raise Exception("Failed to Load configuration file {}: {}".format(filename, e))

	@staticmethod
	def get_immediate_subdirectories(a_dir):
		return [name for name in os.listdir(a_dir) if os.path.isdir(os.path.join(a_dir, name))]
