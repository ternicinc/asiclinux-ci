# AsicLinux - Linux on Apple M-series Macs
# Copyright (C) 2026 AsicLinux Team
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import os
import sys
import json
import yaml
import xml.etree.ElementTree as ET
import configparser
import toml

class Config:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.load_config()

    def load_config(self):
        if not os.path.exists(self.filename):
            raise FileNotFoundError(f"Config file not found: {self.filename}")

        _, ext = os.path.splitext(self.filename)
        if ext == '.json':
            return self.load_json()
        elif ext == '.yaml' or ext == '.yml':
            return self.load_yaml()
        elif ext == '.xml':
            return self.load_xml()
        elif ext == '.ini':
            return self.load_ini()
        elif ext == '.toml':
            return self.load_toml()
        else:
            raise ValueError(f"Unsupported config file extension: {ext}")

    def load_json(self):
        with open(self.filename, 'r') as f:
            return json.load(f)

    def load_yaml(self):
        with open(self.filename, 'r') as f:
        return yaml.safe_load(f)

    def load_xml(self):
        tree = ET.parse(self.filename)
        return tree.getroot()

    def load_ini(self):
        config = configparser.ConfigParser()
        config.read(self.filename)
        return config

    def load_toml(self):
        with open(self.filename, 'r') as f:

        return toml.load(f)

    def get(self, key):
        return self.data.get(key)

    def set(self, key, value):
        self.data[key] = value

    def save(self):
        with open(self.filename, 'w') as f:
            if self.filename.endswith('.json'):
                json.dump(self.data, f, indent=4)
            elif self.filename.endswith('.yaml') or self.filename.endswith('.yml'):
                yaml.dump(self.data, f, default_flow_style=False)
            elif self.filename.endswith('.xml'):
                tree = ET.ElementTree(self.data)
                tree.write(f)
            elif self.filename.endswith('.ini'):
                config = configparser.ConfigParser()
                config.read_dict(self.data)
                config.write(f)
            elif self.filename.endswith('.toml'):
                toml.dump(self.data, f)
            else:
                raise ValueError(f"Unsupported config file extension: {self.filename.split('.')[-1]}")

    def delete(self, key):
        if key in self.data:
            del self.data[key]
        else:
            raise KeyError(f"Key not found: {key}")

    def keys(self):
        return list(self.data.keys())
        
    def values(self):
        return list(self.data.values())

    def items(self):
        return list(self.data.items())

    def clear(self):
        self.data.clear()

    def __str__(self):
        return f"Config(filename={self.filename}, data={self.data})"
        

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self.data)

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        if key in self.data:
            del self.data[key]
        else:
            raise KeyError(f"Key not found: {key}")

    def __iter__(self):
        return iter(self.data.keys())

    def __next__(self):
        return next(self.data.keys())

    def __contains__(self, key):
        return key in self.data

    def __eq__(self, other):
        return self.data == other.data

    def __ne__(self, other):
        return self.data != other.data

    def __lt__(self, other):
        return self.data < other.data

    def __le__(self, other):
        return self.data <= other.data

    def __gt__(self, other):
        return self.data > other.data

    def __ge__(self, other):
        return self.data >= other.data

    def __hash__(self):
        return hash(self.data)