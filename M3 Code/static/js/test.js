Blockly.defineBlocksWithJsonArray([
    {
        type : "move",
        message0: 'move',
        previousStatement: null,
        nextStatement: null,
        colour: 160,
        tooltip: "Return move",

    },
    {
        type: "left",
        message0: 'move left',
        previousStatement: null,
        nextStatement: null,
        colour: 160,
        tooltip: "Return move left",
    },
    {
        type:"red",
        message0:"%1",
        args0:[{
            type:"field_colour",
            name:"COLOUR",
            colour:"#ff0000"
        }],
        output:"Colour",
        style:"colour_blocks",
        extensions: ["set_red_extension"]
    },
    {
        type:"green",
        message0:"%1",
        args0:[{
            type:"field_colour",
            name:"COLOUR",
            colour:"#00ff48"
        }],
        output:"Colour",
        style:"colour_blocks",
        extensions: ["set_green_extension"]
    },
]);

Blockly.Extensions.register('set_green_extension',
  function() {
    var field = this.getField("COLOUR");
    field.setColours(
      ['#00ff48'],
      ['#00ff48']);
  });
  Blockly.Extensions.register('set_red_extension',
  function() {
    var field = this.getField("COLOUR");
    field.setColours(
      ['#ff0000'],
      ['#ff0000']);
  });