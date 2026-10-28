"""An async client for containerd's native v1 API, with plain Python types at its API."""

from importlib.metadata import version

from containerd_client.client import (
    NAMESPACE_HEADER,
    SPEC_TYPE_URL,
    ContainerdAPI,
    ContainerdClient,
)
from containerd_client.errors import (
    BlobNotFound,
    ContainerdCallFailed,
    ContainerdError,
    ContainerdNotFound,
    ContainerdUnavailable,
    ImageNotFound,
    SnapshotParentNotFound,
)
from containerd_client.runtime_options import RUNTIME_OPTIONS_TYPE_URL, config_path_options
from containerd_client.types import (
    DEFAULT_CALL_TIMEOUT,
    ContainerdClientConfig,
    ContainerRecord,
    ImageTarget,
    MountSpec,
    RuntimeOptions,
    TaskInfo,
    TaskState,
)

__version__ = version("containerd-client-py")

__all__ = (
    "DEFAULT_CALL_TIMEOUT",
    "NAMESPACE_HEADER",
    "RUNTIME_OPTIONS_TYPE_URL",
    "SPEC_TYPE_URL",
    "BlobNotFound",
    "ContainerRecord",
    "ContainerdAPI",
    "ContainerdCallFailed",
    "ContainerdClient",
    "ContainerdClientConfig",
    "ContainerdError",
    "ContainerdNotFound",
    "ContainerdUnavailable",
    "ImageNotFound",
    "ImageTarget",
    "MountSpec",
    "RuntimeOptions",
    "SnapshotParentNotFound",
    "TaskInfo",
    "TaskState",
    "config_path_options",
)
