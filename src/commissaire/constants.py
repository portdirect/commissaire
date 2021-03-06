# Copyright (C) 2016  Red Hat, Inc
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
Constants for Commissaire.
"""

#: Cluster type for host nodes only
CLUSTER_TYPE_HOST = 'host_only'
#: Cluster type for host nodes with kubernetes as the container manager
CLUSTER_TYPE_KUBERNETES = 'kubernetes'
#: Cluster type to use if none is specified
CLUSTER_TYPE_DEFAULT = CLUSTER_TYPE_KUBERNETES
#: All cluster types
CLUSTER_TYPES = [CLUSTER_TYPE_HOST, CLUSTER_TYPE_KUBERNETES]

#: Flannel using etcd as it's configuration end
NETWORK_TYPE_FLANNEL_ETCD = 'flannel_etcd'
#: Flannel using a flannel server as it's configuration end
NETWORK_TYPE_FLANNEL_SERVER = 'flannel_server'
#: Network type to use if none is specified
NETWORK_TYPE_DEFAULT = NETWORK_TYPE_FLANNEL_ETCD
#: All network types
NETWORK_TYPES = [NETWORK_TYPE_FLANNEL_ETCD, NETWORK_TYPE_FLANNEL_SERVER]

#: Default network if non is provided
DEFAULT_CLUSTER_NETWORK_JSON = {
    'name': 'default',
    'type': NETWORK_TYPE_DEFAULT
}

# Default etcd configuration
# (server URL provided by store handler)
DEFAULT_ETCD_STORE_HANDLER = {
    'name': 'commissaire.storage.etcd',
    'models': []
}

# Default Kubernetes configuration
# (server URL provided by store handler)
DEFAULT_KUBERNETES_STORE_HANDLER = {
    'name': 'commissaire.store.kubestorehandler',
    'models': ['*']
}

# JSONRPC error codes
JSONRPC_ERRORS = {
    'INVALID_JSON': -32700,
    'INVALID_REQUEST': -32602,
    'METHOD_NOT_FOUND': -32601,
    'INVALID_PARAMETERS': -32602,
    'INTERNAL_ERROR': -32603,
    # Custom codes
    'CONFLICT': 409,
}

#: Expected date format (isoformat)
DATE_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
