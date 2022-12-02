let section = document.getElementById("activtyFeld");

let none = document.getElementById("none");
none.onclick = () => {
	// remove the block input for the activties
	let ruleNum = "second";
	let activty = document.getElementById(ruleNum);
	if (activty) removeAllInputsAt(activty);

	// clear  the input for the activties
	let LTL_rule_2 = document.getElementsByName("LTL_rule_2");
	for (var i = 0; i < LTL_rule_2.length; i++) LTL_rule_2[i].checked = false;

	// remove the rule block 2
	let section2 = document.getElementById("section2");
	section2.style.display = "none";
	document.getElementById("1b").required = false;
};
and.onclick = () => {
	let section2 = document.getElementById("section2");
	section2.style.display = "inline-block";
	document.getElementById("1b").required = true;
};
or.onclick = () => {
	let section2 = document.getElementById("section2");
	section2.style.display = "inline-block";
	document.getElementById("1b").required = true;
};

function createDiv(name) {
	var newDiv = document.createElement("div");
	newDiv.id = name;
	newDiv.className = "activtyFeld";
	if (name == "first") section.prepend(newDiv);
	else section.append(newDiv);

	return newDiv;
}

function createText(ruleNum) {
	let text = document.createElement("h3");
	text.innerHTML = `Now choose the activities of the ${ruleNum} LTL rule:`;
	return text;
}

function createElementText(placeholder, ruleNum) {
	let activty = document.createElement("input");
	activty.required = true;
	activty.className = "activityInput";
	activty.type = "text";
	activty.name = `activitiesOfThe${ruleNum}Rule`;
	activty.placeholder = `activity ${placeholder}`;
	return activty;
}

function createInputAt(numOfActivties, place, ruleNum) {
	for (let index = 0; index < numOfActivties; index++) {
		let chr = String.fromCharCode(65 + index);
		let elm = createElementText(chr, ruleNum);
		place.append(elm);
	}
}

function removeAllInputsAt(place) {
	place.remove();
}

function clickA() {
	let ruleNum = "first";
	let activty = document.getElementById(ruleNum);
	if (activty) removeAllInputsAt(activty);
	let newDiv = createDiv(ruleNum);
	newDiv.prepend(createText(ruleNum));
	createInputAt(1, newDiv, ruleNum);
}

function clickAB() {
	let ruleNum = "first";
	let activty = document.getElementById(ruleNum);
	if (activty) removeAllInputsAt(activty);
	let newDiv = createDiv(ruleNum);
	newDiv.prepend(createText(ruleNum));
	createInputAt(2, newDiv, ruleNum);
}

function clickABC() {
	let ruleNum = "first";
	let activty = document.getElementById(ruleNum);
	if (activty) removeAllInputsAt(activty);
	let newDiv = createDiv(ruleNum);
	newDiv.prepend(createText(ruleNum));
	createInputAt(3, newDiv, ruleNum);
}

function clickABCD() {
	let ruleNum = "first";
	let activty = document.getElementById(ruleNum);
	if (activty) removeAllInputsAt(activty);
	let newDiv = createDiv(ruleNum);
	newDiv.prepend(createText(ruleNum));
	createInputAt(4, newDiv, ruleNum);
}

function clickA_2() {
	let ruleNum = "second";
	let activty = document.getElementById(ruleNum);
	if (activty) removeAllInputsAt(activty);
	let newDiv = createDiv(ruleNum);
	newDiv.prepend(createText(ruleNum));
	createInputAt(1, newDiv, ruleNum);
}

function clickAB_2() {
	let ruleNum = "second";
	let activty = document.getElementById(ruleNum);
	if (activty) removeAllInputsAt(activty);
	let newDiv = createDiv(ruleNum);
	newDiv.prepend(createText(ruleNum));
	createInputAt(2, newDiv, ruleNum);
}

function clickABC_2() {
	let ruleNum = "second";
	let activty = document.getElementById(ruleNum);
	if (activty) removeAllInputsAt(activty);
	let newDiv = createDiv(ruleNum);
	newDiv.prepend(createText(ruleNum));
	createInputAt(3, newDiv, ruleNum);
}

function clickABCD_2() {
	let ruleNum = "second";
	let activty = document.getElementById(ruleNum);
	if (activty) removeAllInputsAt(activty);
	let newDiv = createDiv(ruleNum);
	newDiv.prepend(createText(ruleNum));
	createInputAt(4, newDiv, ruleNum);
}
