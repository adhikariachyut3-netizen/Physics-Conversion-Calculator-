const conversions = {
  length: [
    { from: 'Centimeter', to: 'Meter', factor: 0.01 },
    { from: 'Meter', to: 'Centimeter', factor: 100 },
    { from: 'Kilometer', to: 'Meter', factor: 1000 },
    { from: 'Meter', to: 'Kilometer', factor: 0.001 },
  ],
  time: [
    { from: 'Second', to: 'Hour', factor: 1 / 3600 },
    { from: 'Second', to: 'Minute', factor: 1 / 60 },
    { from: 'Minute', to: 'Second', factor: 60 },
    { from: 'Minute', to: 'Hour', factor: 1 / 60 },
    { from: 'Day', to: 'Minute', factor: 24 * 60 },
  ],
  velocity: [
    { from: 'Meter/second', to: 'Centimeter/second', factor: 100 },
    { from: 'Centimeter/second', to: 'Meter/second', factor: 0.01 },
    { from: 'Kilometer/hour', to: 'Meter/second', factor: 1 / 3.6 },
    { from: 'Meter/second', to: 'Kilometer/hour', factor: 3.6 },
  ],
  force: [
    { from: 'Newton', to: 'Kilogram·meter/second²', factor: 1 },
    { from: 'Kilogram·meter/second²', to: 'Newton', factor: 1 },
    { from: 'Newton', to: 'Dyne', factor: 100000 },
    { from: 'Dyne', to: 'Newton', factor: 1 / 100000 },
  ],
};

const quantitySelect = document.querySelector('#quantity');
const conversionSelect = document.querySelector('#conversion');
const valueInput = document.querySelector('#value');
const form = document.querySelector('#converter-form');
const resultValue = document.querySelector('#result-value');
const resultEquation = document.querySelector('#result-equation');
const errorMessage = document.querySelector('#error-message');

function formatNumber(number) {
  return new Intl.NumberFormat(undefined, { maximumSignificantDigits: 7 }).format(number);
}

function populateConversions() {
  const options = conversions[quantitySelect.value];
  conversionSelect.replaceChildren(...options.map((item, index) => {
    const option = document.createElement('option');
    option.value = String(index);
    option.textContent = `${item.from} → ${item.to}`;
    return option;
  }));
  clearResult();
}

function clearResult() {
  resultValue.textContent = '—';
  resultEquation.textContent = 'Your converted value will appear here.';
  errorMessage.textContent = '';
}

quantitySelect.addEventListener('change', populateConversions);
valueInput.addEventListener('input', () => { errorMessage.textContent = ''; });

form.addEventListener('submit', (event) => {
  event.preventDefault();
  const value = valueInput.valueAsNumber;
  if (valueInput.value.trim() === '' || !Number.isFinite(value)) {
    errorMessage.textContent = 'Enter a valid number to convert.';
    valueInput.focus();
    return;
  }

  const conversion = conversions[quantitySelect.value][Number(conversionSelect.value)];
  const result = value * conversion.factor;
  if (!Number.isFinite(result)) {
    errorMessage.textContent = 'That value is too large to convert.';
    return;
  }

  errorMessage.textContent = '';
  resultValue.textContent = `${formatNumber(result)} ${conversion.to}`;
  resultEquation.textContent = `${formatNumber(value)} ${conversion.from} = ${formatNumber(result)} ${conversion.to}`;
});

populateConversions();
