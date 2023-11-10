# Copyright 2023 Avaiga Private Limited
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.

from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from sqlalchemy import JSON, Boolean, Column, String, Table

from .._repository._base_taipy_model import _BaseModel
from .._repository.db._sql_base_model import mapper_registry
from ..cycle.cycle_id import CycleId
from ..data.data_node_id import DataNodeId
from ..task.task_id import TaskId
from .scenario_id import ScenarioId


@mapper_registry.mapped
@dataclass
class _ScenarioModel(_BaseModel):
    __table__ = Table(
        "scenario",
        mapper_registry.metadata,
        Column("id", String, primary_key=True),
        Column("config_id", String),
        Column("tasks", JSON),
        Column("additional_data_nodes", JSON),
        Column("properties", JSON),
        Column("creation_date", String),
        Column("primary_scenario", Boolean),
        Column("subscribers", JSON),
        Column("tags", JSON),
        Column("version", String),
        Column("sequences", JSON),
        Column("cycle", String),
    )
    id: ScenarioId
    config_id: str
    tasks: List[TaskId]
    additional_data_nodes: List[DataNodeId]
    properties: Dict[str, Any]
    creation_date: str
    primary_scenario: bool
    subscribers: List[Dict]
    tags: List[str]
    version: str
    sequences: Optional[Dict[str, Dict]] = None
    cycle: Optional[CycleId] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]):
        return _ScenarioModel(
            id=data["id"],
            config_id=data["config_id"],
            tasks=_BaseModel._deserialize_attribute(data["tasks"]),
            additional_data_nodes=_BaseModel._deserialize_attribute(data["additional_data_nodes"]),
            properties=_BaseModel._deserialize_attribute(data["properties"]),
            creation_date=data["creation_date"],
            primary_scenario=data["primary_scenario"],
            subscribers=_BaseModel._deserialize_attribute(data["subscribers"]),
            tags=_BaseModel._deserialize_attribute(data["tags"]),
            version=data["version"],
            sequences=_BaseModel._deserialize_attribute(data["sequences"]),
            cycle=CycleId(data["cycle"]) if "cycle" in data else None,
        )

    @staticmethod
    def to_list(model):
        return [
            model.id,
            model.config_id,
            _BaseModel._serialize_attribute(model.tasks),
            _BaseModel._serialize_attribute(model.additional_data_nodes),
            _BaseModel._serialize_attribute(model.properties),
            model.creation_date,
            model.primary_scenario,
            _BaseModel._serialize_attribute(model.subscribers),
            _BaseModel._serialize_attribute(model.tags),
            model.version,
            _BaseModel._serialize_attribute(model.sequences),
            model.cycle,
        ]
