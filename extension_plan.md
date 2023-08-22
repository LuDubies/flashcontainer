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


## Review
