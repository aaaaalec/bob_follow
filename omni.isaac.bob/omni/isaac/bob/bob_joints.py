from typing import List, Optional
import carb
import numpy as np
from omni.isaac.core.prims.rigid_prim import RigidPrim
from omni.isaac.core.robots.robot import Robot
from omni.isaac.core.utils.prims import get_prim_at_path
from omni.isaac.core.utils.stage import add_reference_to_stage

class BobJoints(Robot):
    """Robot class for Bob Joints robot
    
    Args:
        prim_path (str): The prim path of the robot in the stage
        name (str, optional): Name of the robot. Defaults to "bob_joints_robot".
        usd_path (Optional[str], optional): Path to the USD file. Defaults to None.
        position (Optional[np.ndarray], optional): Initial position. Defaults to None.
        orientation (Optional[np.ndarray], optional): Initial orientation. Defaults to None.
        end_effector_prim_name (Optional[str], optional): Name of end effector prim. Defaults to None.
    """
    def __init__(
        self,
        prim_path: str,
        name: str = "bob_joints_robot",
        usd_path: Optional[str] = None,
        position: Optional[np.ndarray] = None,
        orientation: Optional[np.ndarray] = None,
        end_effector_prim_name: Optional[str] = None,
    ) -> None:
        prim = get_prim_at_path(prim_path)
        self._end_effector = None
        if not prim.IsValid():
            if usd_path:
                add_reference_to_stage(usd_path=usd_path, prim_path=prim_path)
            else:
                usd_path = "/home/space/ws_moveit/src/bob_joints_description/urdf/bob_joints/bob_joints.usd"
                add_reference_to_stage(usd_path=usd_path, prim_path=prim_path)
            
            if end_effector_prim_name is None:
                self._end_effector_prim_path = prim_path + "/brush_1"
            else:
                self._end_effector_prim_path = prim_path + "/" + end_effector_prim_name
        else:
            if end_effector_prim_name is None:
                self._end_effector_prim_path = prim_path + "/brush_1"
            else:
                self._end_effector_prim_path = prim_path + "/" + end_effector_prim_name

        super().__init__(
            prim_path=prim_path, name=name, position=position, orientation=orientation, articulation_controller=None
        )
        return

    @property
    def end_effector(self) -> RigidPrim:
        """Get the end effector rigid prim
        
        Returns:
            RigidPrim: The end effector rigid prim
        """
        return self._end_effector

    def initialize(self, physics_sim_view=None) -> None:
        """Initialize the robot"""
        super().initialize(physics_sim_view)
        self._end_effector = RigidPrim(prim_path=self._end_effector_prim_path, name=self.name + "_end_effector")
        self._end_effector.initialize(physics_sim_view)
        return