from typing import Optional
import omni.isaac.motion_generation.interface_config_loader as interface_config_loader
from omni.isaac.core.articulations import Articulation
from omni.isaac.motion_generation.articulation_kinematics_solver import ArticulationKinematicsSolver
from omni.isaac.motion_generation.lula.kinematics import LulaKinematicsSolver

class KinematicsSolver(ArticulationKinematicsSolver):
    """Kinematics Solver for Bob Joints robot
    
    Args:
        robot_articulation (Articulation): An initialized Articulation object
        end_effector_frame_name (Optional[str]): The name of the end effector frame
    """
    def __init__(self, robot_articulation: Articulation, end_effector_frame_name: Optional[str] = None) -> None:
        kinematics_config = interface_config_loader.load_supported_lula_kinematics_solver_config("BobJoints")
        self._kinematics = LulaKinematicsSolver(**kinematics_config)
        if end_effector_frame_name is None:
            end_effector_frame_name = "brush_1"
        ArticulationKinematicsSolver.__init__(self, robot_articulation, self._kinematics, end_effector_frame_name)
        return