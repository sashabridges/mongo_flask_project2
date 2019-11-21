function init() {
    // Grab a reference to the dropdown select element
    var selector = d3.select("#misc_list");
  
    // Use the list of sample names to populate the select options
    d3.json("/names").then(sampleNames => {
      sampleNames.forEach((sample) => {
        selector
          .append("li")
          .append("list-group-item")
          .text(sample)
          .property("value", sample);
      });
  
      // Use the first sample from the list to build the initial plots
      //const firstSample = sampleNames[0];
    });
  }
init();