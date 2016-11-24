#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from mock import MagicMock, Mock, patch
import sys
sys.modules['creds'] = Mock()
