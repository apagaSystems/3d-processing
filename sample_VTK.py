# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkIOGeometry import vtkSTLReader
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)


def main():
    colors = vtkNamedColors()

    reader = vtkSTLReader()
    reader.SetFileName('./models/nut.stl')

    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(reader.GetOutputPort())

    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetDiffuse(0.8)
    actor.GetProperty().SetDiffuseColor(colors.GetColor3d('LightSteelBlue'))
    actor.GetProperty().SetSpecular(0.3)
    actor.GetProperty().SetSpecularPower(60.0)

    # Create a rendering window and renderer
    ren = vtkRenderer()
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren)
    renWin.SetWindowName('ReadSTL')

    # Create a renderwindowinteractor
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    # Assign actor to the renderer
    ren.AddActor(actor)
    ren.SetBackground(colors.GetColor3d('DarkOliveGreen'))

    # Enable user interface interactor
    iren.Initialize()
    renWin.Render()
    iren.Start()


if __name__ == '__main__':
    main()