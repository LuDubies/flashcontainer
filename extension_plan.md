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
* Include arrays of fixed size in the struct
* Include padding elements to align fields of the struct
* enable translation into a C-type struct
* enable translation into pyHexdump config

## Implementation Details

This chapter will slightly structure the features and design choices made. It is also designed to feature the necessary documentation to be integrated into
the full README on feature merge.

The overall XML structure will be extended to feature struct elements that are defined outside of the containers that define the memory layout.

        <pd:struct>
            <pd:fields>
                <pd:field>
                ...
                <pd:arrayfield>
                ...
                <pd:padding>
            </pd:fields>
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
| fill             | Byte value used for padding  |   Yes  |  parent |


The fill value will be used as padding, with the additional options of "parent".
Choosing **parent** will use the fill value of a parameters encompassing block.

### The Field Element

A field is the basic building block of a struct and serves as a placeholder for a value of a basic type in instances of the struct.
Unlike parameter elements in a block, a field does not hold offset or alignment information, instead alignment is handled by padding tags.
The basic type of the field defines its size and content interpretation.

|Attribute         |Description                   |optional| default |
|------------------|------------------------------|--------|---------|
| name             | The fields name.             |   No   |         |
| type             | Basic type of the field      |   No   |         |


### The Array Field Element

Array Fields are similar to fields, but feature a size attribute that determines the resulting arrays size

|Attribute         |Description                   |optional| default |
|------------------|------------------------------|--------|---------|
| name             | The fields name.             |   No   |         |
| type             | Basic type of the field      |   No   |         |
| size             | Size of the array            |   No   |         |

### The Padding Element

The padding element is used to introduce gaps / offsets between a structs fields. It features a size attribute that determines the padding size.
|Attribute         |Description                   |optional| default |
|------------------|------------------------------|--------|---------|
| size             | Size of the array            |   No   |         |


### Appendix To Parameter Element

Added the struct attribute to the parameter element, designating the struct to use when the type of the parameter is set to "complex".

|Attribute         |Description                   |optional| default |
|------------------|------------------------------|--------|---------|
| struct           | Struct of the parameter      |   Yes  |    ""   |

## Additional Notes
Additional changes that might be needed for integrating the new feature:

* Adjust pargen XSD version numbering (old XML will stay valid, but new features deserve at least a new minor version)
* Introduce JSON syntax for supplying parameters with values
* Introduce strict array size limits for standard parameters also????
* IMPORTANT: introduce includes for structs into xml syntax


## Additional Feature Ideas

* Random padding bytes
* C-struct like alignment


## Review


