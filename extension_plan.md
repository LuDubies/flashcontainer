# Struct Extension

## Project Goals

This project aims to extend the existing flashcontainer project to include data structures. flashcontainer so far only works with
basic data types.
Including structs would possibly allow for easier XML creation, increase code reusability, as well as the possibility to provide
additional information and output for/with the different output writers and formats.

The addition of new functionality should not negatively impact other features of the project,
additionally changes to code that is not directly affected by the introduction of structs is to be kept to a minimum.

Disregarding the previous paragraph, work in this project will also include the fixing of typos and small code improvements. These are not part of the Extension and might be
discussed and merged separately. 

## Targeted Changes

The inclusion of structs requires extending the XDS base for the pargen XML.
The XML needs to feature a way to describe structs, their , well... , structure and some attributes.
Additionally, paragen parameters need to be extended to allow the use of struct datatypes and efficiently fill the multiple fields with content.

The parser will have to be extended to extract struct information.
Additionaly parsed parameters need to still provide their original fields (value), as well as struct type information if applicable.

Multiple Writers will have to be extended, most importantly the C-Writer and the pyHexdump Writer, to allow for usage and output of the new data.

Tests need to cover the new XML/XSD format, the new parser features and the writer extensions.
Additionally, other tests might be extended to ensure the new feature does not break any previous functionality.

## Struct Required Features

The newly introduced data structure "struct" has to cover these functionalities

* Include one or multiple fields of basic types
* hold information to reference the struct
* enable translation into a C-type struct
* enable translation into pyHexdump config
* adjustable self-alignment
* adjustable struct-alignment
* adjustable stride-address

## Implementation Details

This chapter will slightly structure the features and design choices made. It is also designed to feature the necessary documentation to be integrated into
the full README on feature merge.

The overall XML structure will be extended to feature struct elements that are defined outside of the containers that define the memory layout.

        <pd:struct>
            <pd:parameter>
            ...
        </pd:struct>
        <pd:container>
            <pd:blocks>
                <pd:block>
                    <pd:parameter> or <pd:crc>
                    ...
                </pd:block>
                ...
            </pd:blocks>
            ...
        </pd:container>

### The Struct Element

A **struct** is a way to group multiple simple types into a combined data structure. By referencing a structs name in a block parameter,
the parameters type will be interpreted as the struct. A struct features multiple attributes that define how the struct and the data of the encompassed fields.

|Attribute         |Description                   |optional| default |
|------------------|------------------------------|--------|---------|
| name             | The structs name.            |   No   |         |
| fill             | byte value used for padding  |   Yes  |  parent |
| field_alignment  | apply field alignment        |   Yes  |   True  |
| struct_alignment | apply struct alignment       |   Yes  |   True  |
| stride           | apply stride buffer          |   Yes  |   True  |

Field alignment will ensure that the data of the structs fields is self aligned **relative to the structs address**.
This means that 2 byte data types can only start at 2 byte offsets to the struct address (4 byte types at 4 byte offsets, ...).
Struct alignment will apply a similar constraint to the starting address of the struct. Here the valid addresses are constrained by the size of the biggest field in the struct.
A struct encompassing a uint64 field can only start at addresses divisible by 8 for example.
Application of field and struct alignment will ensure pargen structs feature the same memory layout as C-structs.
Additionally, the stride parameter will result in additional padding up to the structs stride address (the address where the next struct of the same type could start in memory).

The fill value will be used as padding, with the additional options of "parent" and "random".
Choosing **parent** will use the fill value of a parameters encompassing block, the **random** option will randomly fill the padding bytes.

The total memory footprint / size of the struct is highly dependent on the chosen alignment options, as they might result in padding bytes between and after the fields of the struct.
While most compilers for almost all instruction sets and architectures will feature self alignment of C-structs, the options can also be switched of to result in densely packed data in memory.

## Additional Notes

Additional changes that might be needed for integrating the new feature:

* Adjust pargen XSD version numbering (old XML will stay valid, but new features deserve at least a new minor version)



## Review


