# containerd-client-py

An async client (`grpc.aio`) for [containerd](https://containerd.io)'s native v1 gRPC API. Its API uses
plain Python types (dataclasses, `bytes` for serialized messages); no protobuf type crosses it.
Python >= 3.13. Import name: `containerd_client`.

```python
from containerd_client import ContainerdClient, ContainerdClientConfig

client = ContainerdClient(
    ContainerdClientConfig(
        address="/run/containerd/containerd.sock",
        namespace="default",
        snapshotter="overlayfs",
    )
)
await client.connect()
records = await client.list_containers({"owner": "me"})
await client.close()
```

Failures raise `containerd_client.ContainerdError` subclasses (`ContainerdUnavailable`,
`ImageNotFound`, `BlobNotFound`, `SnapshotParentNotFound`, `ContainerdCallFailed`); callers map them
to their own error types.

## containerd API version

The stubs in `src/containerd_client/_grpcapi/` are generated from the protos of containerd
**v1.7.27** (API module v1.8.0) with grpcio-tools **1.84.1** (protobuf gencode 7.35.1). Both are
constants at the top of `scripts/regen.py`.

RPCs the client calls:

- containers: Create, Delete, Get, List
- content: Read
- images: Get
- snapshots: Prepare, Remove
- tasks: Create, Delete, Get, Kill, Start

`config_path_options()` builds a `runtimeoptions.v1.Options` message for shims such as Kata.

## Regenerating the stubs

    uv sync
    uv run python scripts/regen.py     # set CONTAINERD_SRC to reuse a checkout at that tag

To move to another containerd release, change `CONTAINERD_TAG` (and `GRPCIO_TOOLS_VERSION` if
needed, together with the `grpcio-tools` pin in `pyproject.toml`), regenerate, and run the tests.

### protobuf gencode and runtime

Generated code embeds a protobuf runtime version check: the gencode version must be <= the
installed runtime and of the same major version, hence `protobuf>=7.35.1,<8`. Regenerate with a
matching grpcio-tools when consumers move protobuf to a new major version.

## Development

    uv sync
    uv run pytest -q
    uv run ruff check && uv run ruff format --check
    uv run mypy src

## Releasing

1. Set `version` in `pyproject.toml` to `x.y.z` and commit it as `release: x.y.z`.
2. Tag that commit `x.y.z` and push the tag.
3. CI runs the tests, checks that the tag equals the package version, builds the sdist and wheel,
   and publishes them to PyPI through trusted publishing (GitHub environment `deploy-to-pypi`).

## License

Apache-2.0; see `LICENSE` and `NOTICE`. The generated code is compiled from containerd's protos,
which are Apache-2.0.
