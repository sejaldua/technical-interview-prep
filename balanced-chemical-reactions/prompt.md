## Prompt

For a chemical reaction represented by a string, verify that the chemical
reaction is a balanced reaction (i.e. that we didn't somehow lose or gain
an atom during reaction). If the reaction is balanced return true,
otherwise return false.

## Examples

For example, for the hydrogen combustion reaction:

```
2 H2 + O2 -> 2 H2O
```    
would output true because the number of atoms in the reactants match up
with the number of atoms in the product.

However, for the precipitation of silver-chloride:

```
NaCl + AgNO3 -> NaNO3 + Ag
```  
the output should be false because we're missing the chlorine atom in
the products.

The reactancts and products will always be separated by a right
pointing arrow "->" and the individual molecules within the
reactants/products are always separated by a "+" sign. Multiple
molecules are represented by a number and space prefacing the
molecule (e.g., "2 H20").

Other test cases:

```
O2 -> NaCl = false  
C6H12O6 + 6 O2 -> 6 CO2 + 6 H2O = true  
10 NH3 + 10 H2O -> 10 NH4 + OH = false  
```