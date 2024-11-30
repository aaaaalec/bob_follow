from typing import Optional
import numpy as np
import omni.isaac.core.tasks as tasks
from omni.isaac.core.utils.prims import is_prim_path_valid
from omni.isaac.core.utils.string import find_unique_string_name
from omni.isaac.bob import BobJoints

class FollowTarget(tasks.FollowTarget):
    """Follow target task for Bob Joints robot
    
    Args:
        name (str, optional): Task name. Defaults to "bob_joints_follow_target".
        target_prim_path (Optional[str], optional): Target prim path. Defaults to None.
        target_name (Optional[str], optional): Target name. Defaults to None.
        target_position (Optional[np.ndarray], optional): Target position. Defaults to None.
        target_orientation (Optional[np.ndarray], optional): Target orientation. Defaults to None.
        offset (Optional[np.ndarray], optional): Target offset. Defaults to None.
        robot_prim_path (Optional[str], optional): Robot prim path. Defaults to None.
        robot_name (Optional[str], optional): Robot name. Defaults to None.
    """
    def __init__(
        self,
        name: str = "bob_joints_follow_target",
        target_prim_path: Optional[str] = None,
        target_name: Optional[str] = None,
        target_position: Optional[np.ndarray] = None,
        target_orientation: Optional[np.ndarray] = None,
        offset: Optional[np.ndarray] = None,
        robot_prim_path: Optional[str] = None,
        robot_name: Optional[str] = None,
    ) -> None:
        tasks.FollowTarget.__init__(
            self,
            name=name,
            target_prim_path=target_prim_path,
            target_name=target_name,
            target_position=target_position,
            target_orientation=target_orientation,
            offset=offset,
        )
        self._robot_prim_path = robot_prim_path
        self._robot_name = robot_name
        return

    def set_robot(self) -> BobJoints:
        """Set up the robot instance
        
        Returns:
            BobJoints: The robot instance
        """
        if self._robot_prim_path is None:
            self._robot_prim_path = find_unique_string_name(
                initial_name="/World/bob_joints", is_unique_fn=lambda x: not is_prim_path_valid(x)
            )
        if self._robot_name is None:
            self._robot_name = find_unique_string_name(
                initial_name="my_bob_joints", is_unique_fn=lambda x: not self.scene.object_exists(x)
            )
        return BobJoints(prim_path=self._robot_prim_path, name=self._robot_name)