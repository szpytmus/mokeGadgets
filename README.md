# Tools for MOKE microscopy - Hysteresis Loop parameters Extraction

Using magneto-optical physical effects, we can measure ferromagnetic hysteresis loops with a specialized microscopy setup. Magnetic hysteresis loops for ferromagnets are precious source of underlying magnetic properties. Especially in thin layered structures. Most often magnetic hysteresis loops provide basic information about the layered system with a ferromagnet. From such loops parameters like: Remanence(REM) - residual magnetization in zero field, Coercivity (H~C~) - the width of the loop and Exchange Bias (H~EB~) in case of the FM/AFM bilayers visible as horizontal shift of the hysteresis loop relative to the zero field axis can be extracted. Most measurement softwares for microscopes do not provide tools to calculate such parameters from the loops. This App is a stack of tools facilitating such calculations. 


![Exemplary magnetic hysteresis loop with necessary paramenters](https://github.com/szpytmus/mokeGadgets/assets/62251445/34a4a7c3-ebd8-4633-8023-073bc63f76be~'Exemplary hysteresis loop')

Formulas for:
Remanence = (REM~max~ - REM~min~)/(SAT~max~ - SAT~min~)
Coercivity = (H~C2~ - H~C2~)/2
Exchange Bias = (H~C2~ + H~C2~)/2

The App is provided with a Tkinter GUI, with a calculator for:
- Remanence
- Coercivity (:hammer_and_wrench: WORK IN PROGRESS! :hammer_and_wrench:)
- Exchange Bias (:hammer_and_wrench: WORK IN PROGRESS! :hammer_and_wrench:)

  


