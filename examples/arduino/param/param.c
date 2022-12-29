/* AUTOGENERATED by pargen 0.1.0 2022-12-29 14:45:11.179604
 * cmd: /Users/norbert/proj/flashcontainer/.venv/bin/pargen --ihex --csrc --gld --destdir param param/param.xml
 * Buildkey: 538f7828-2b36-4b17-b013-b588cebd371e
 * !! DO NOT EDIT MANUALLY !!
 */

#include "param.h"

/* BEGIN Block par in container EEPROM @ 0x81000000
 *
 * 1Kb Example parameter block for displaying a flashable message with update delay
 */
volatile const pargen_header_type_t par_blkhdr =
{
    0x00EE,
    0x0001,
    0x0000,
    0x0001,
    0x00000000,
    0x00000400,
};

/* Parameter par_UpdateDelay_ms @ 0x81000010
 * Interval time between dumping welcome message.
 */
volatile const uint16_t par_UpdateDelay_ms = 0x07D0;

/* Parameter par_WelcomeMsg_str @ 0x81000012
 * Message to display in endless loop.
 */
volatile const char par_WelcomeMsg_str[49] = 
{
    0x54, 0x68, 0x69, 0x73, 
    0x20, 0x6D, 0x65, 0x73, 
    0x73, 0x61, 0x67, 0x65, 
    0x20, 0x69, 0x73, 0x20, 
    0x64, 0x65, 0x66, 0x69, 
    0x6E, 0x65, 0x64, 0x20, 
    0x61, 0x73, 0x20, 0x61, 
    0x20, 0x50, 0x61, 0x72, 
    0x67, 0x65, 0x6E, 0x20, 
    0x70, 0x61, 0x72, 0x61, 
    0x6D, 0x65, 0x74, 0x65, 
    0x72, 0x21, 0x0D, 0x0A, 
    0x00
};

/* Parameter par_crc @ 0x810003fc
 * crc: 0x81000000-0x810003FB  polynomial:0x4C11DB7, 32 Bit, init:0xFFFFFFFF, reverse in:True, reverse out:True, final xor:True, access:1, swap:False
 */
volatile const uint32_t par_crc = 0xC3853376;

/* END Block par
 */

