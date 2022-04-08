import os
import json
import logging
import logging.handlers

class Utils:

	@staticmethod
	def register_handlers(file_log_level: str, log_path: str) -> None:
		"""
		Register all log handlers

		Register a file handler for the application as a default logger with settings form the configuration\
		Register a console handler. Default is on ERROR level.

		:return:
		"""
		# Set root Log Level to DEBUG so that all logs are passed to the handlers
		logging.getLogger().setLevel('DEBUG')
		# Create File handler
		# File handler logs on configured log level to file
		file_handler = Utils.register_file_handler(file_log_level=file_log_level, log_path=log_path)
		logging.getLogger().addHandler(file_handler)

		# Create Console Handler
		# Console handler logs on ERROR as default
		console_handler = Utils.register_console_handler()
		logging.getLogger().addHandler(console_handler)

	@staticmethod
	def register_file_handler(log_path: str, file_log_level: str) -> logging.FileHandler:
		formatter = logging.Formatter('{asctime} {name} {levelname:8s} {message}', style='{')
		handler = logging.handlers.RotatingFileHandler(filename=log_path,
													   backupCount=30,
													   maxBytes=10000)  # 10kb
		handler.setFormatter(formatter)
		handler.setLevel(file_log_level)
		return handler

	@staticmethod
	def register_console_handler() -> logging.StreamHandler:
		handler = logging.StreamHandler()
		handler.setLevel("ERROR")
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
			raise Exception("Failed to Load configuration file {}: {}".format(filename,e))
