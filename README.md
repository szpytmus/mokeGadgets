# Tools for MOKE microscopy - Hysteresis Loop parameters Extraction

Using magneto-optical physical effects, we can measure ferromagnetic hysteresis loops with a specialized microscopy setup. Magnetic hysteresis loops for ferromagnets are precious source of underlying magnetic properties. Especially in thin layered structures. Most often magnetic hysteresis loops provide basic information about the layered system with a ferromagnet. From such loops parameters like: Remanence(REM) - residual magnetization in zero field, Coercivity (HC) - the width of the loop and Exchange Bias (HEB) in case of the FM/AFM bilayers visible as horizontal shift of the hysteresis loop relative to the zero field axis can be extracted. Most measurement softwares for microscopes do not provide tools to calculate such parameters from the loops. This App is a stack of tools facilitating such calculations. 


![Exemplary magnetic hysteresis loop with necessary paramenters](https://github.com/szpytmus/mokeGadgets/assets/62251445/34a4a7c3-ebd8-4633-8023-073bc63f76be)

Formulas for:
Remanence = (REMmax - REMmin)/(SATmax - SATmin)
Coercivity = (HC2 - HC2)/2
Exchange Bias = (HC2 + HC2)/2

The App is provided with a Tkinter GUI, with a calculator for:
- Remanence
- Coercivity (:hammer_and_wrench: WORK IN PROGRESS! :hammer_and_wrench:)
- Exchange Bias (:hammer_and_wrench: WORK IN PROGRESS! :hammer_and_wrench:)


Plans for future development:
- Finish Coercivity and Exchange Bias calculation Features
- Add feature to visualize magnetic hysteresis loops in the GUI
- Interactive parameter data selection from visualized loop

Technologies used:
- Tkinter
- Object-Oriented Programming Concepts

## Instruction to create executable mokeGadgetsTool from a script using PyInstaller

1. Download mokeGadgetsTool.py to a relevant location
2. Using Command Prompt cd your directory with the script
3. Execute PyInstaller command: `pyinstaller --onefile mokeGadgetsTool.py`
4. Enjoy and use freely the .exe file

  


