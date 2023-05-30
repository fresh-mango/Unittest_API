#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
日志类。通过读取配置文件，定义日志级别、日志文件名、日志格式等。
一般直接把logger import进去
from utils.log import logger
logger.info('test log')
"""
import time
import os
import logging
from logging.handlers import TimedRotatingFileHandler
from utils.config import ParserConfig,log_path


class Logger(object):
    def __init__(self, logger_name=None):
        self.name = logger_name
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(logging.INFO)

        self.parser = ParserConfig()
        self.log_file_name = self.parser.get_section_options('log','file_name')
        self.backup_count = self.parser.get_section_options('log','backup')
        self.console_output_level = self.parser.get_section_options('log','console_level')
        self.file_output_level = self.parser.get_section_options('log','file_level')
        #pattern = self.parser.get_section_options('log', 'pattern') if self.parser  else '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'
        pattern = '%(asctime)s - %(filename)s  - [line:%(lineno)d] - %(levelname)s: %(message)s'
        self.formatter = logging.Formatter(pattern)

        if not self.logger.handlers:
            rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)

            # 每天重新创建一个日志文件，最多保留backup_count份
            file_handler = TimedRotatingFileHandler(filename=os.path.join(log_path, rq + self.log_file_name),
                                                    when='D',
                                                    interval=1,
                                                    backupCount=self.backup_count,
                                                    delay=True,
                                                    encoding='utf-8'
                                                    )
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)


    def get_logger(self):
        return self.logger


if __name__ == "__main__":
    l = Logger()
    data = l.get_logger()
    print('AAA',data.info('你好'))

