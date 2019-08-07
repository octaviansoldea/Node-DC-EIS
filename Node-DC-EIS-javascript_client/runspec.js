'use strict';

/*let yargs = require('yargs');
yargs.default('x', 10).alias('x', 'xx').describe('x', 'choose your sandwich ingredients')
const args = yargs.argv;

console.log('x: ' + args.x);
console.log('Name: ' + args.name);
console.log('Age: ' + args.age);
*/

/*
let yargs = require('yargs');
yargs.options({
  'x': {
    default: 10,
    alias: ['xx', 'yyyy'],
    describe: 'choose your sandwich ingredients'
}})
const args = yargs.argv;

console.log('args.x: ' + args.x);
console.log('args.xx: ' + args.xx);
console.log('args.yyyy: ' + args.yyyy);
console.log('Name: ' + args.name);
console.log('Age: ' + args.age);

*/

let yargs = require('yargs');

yargs.options({
  'id': {
    default: 0,
    alias: 'instanceID',
    describe: 'Instance ID'
}})

yargs.options({
  'ng': {
    default: 0,
    alias: 'nograph',
    describe: 'Show graph option'
}})

yargs.options({
  'm': {
    default: true,
    alias: ['multiple'],
    describe: 'Multiple instance run'
}})

yargs.options({
  'dir': {
    default: "",
    alias: ['directory', 'rundir'],
    describe: 'The log directory'
}})

yargs.options({
  'o': {
    default: "",
    alias: ['output', 'output_filename'],
    describe: 'The output file name'
}})

yargs.options({
  'f': {
    default: "config.json",
    alias: 'config',
    describe: 'The configuration file to be used'
}})

yargs.options({
  't': {
    default: 100,
    alias: 'MT_interval',
    describe: 'Runtime in Seconds'
}})

yargs.options({
  'n': {
    default: 10000,
    alias: 'request',
    describe: 'Number of requests to perform'
}})

yargs.options({
  'c': {
    default: 200,
    alias: 'concurrency',
    describe: 'Number of multiple requests to perform'
}})

yargs.options({
  'W': {
    default: 200,
    alias: ['rampup_rampdown'],
    describe: 'Number of rampup-rampdown requests to perform'
}})

yargs.options({
  'r': {
    default: 1,
    alias: 'run_mode',
    type: 'number',
    choices : [1, 2],
    describe: '1 for time based run. 2 for request based run. Default is 1'
}})

yargs.options({
  'int': {
    default: 10,
    alias: 'interval',
    describe: 'Interval after which logging switches to next temp log file'
}})

yargs.options({
  'log': {
    default: 10,
    alias: ['templogfile', 'templogfile'],
    describe: 'The temporary log file to be used'
}})

yargs.options({
  'idr': {
    default: 50,
    alias: 'idurl_ratio',
    describe: 'The percentage of ID urls to be loaded in URL file'
}})

yargs.options({
  'nur': {
    default: 25,
    alias: 'nameurl_ratio',
    describe: 'The percentage of name urls to be loaded in URL file'
}})

yargs.options({
  'zur': {
    default: 50,
    alias: 'nameurl_ratio',
    describe: 'The percentage of zip urls to be loaded in URL file'
}})

yargs.options({
  'dbc': {
    default: 10000,
    alias: 'dbcount',
    describe: 'The record count to load database'
}})

yargs.options({
  'nr': {
    default: 5,
    alias: 'name_dbratio',
    describe: 'The name ratio'
}})

yargs.options({
  'zr': {
    default: 5,
    alias: 'zip_dbratio',
    describe: 'The zip ratio'
}})

yargs.options({
  'H': {
    default: false,
    alias: 'html',
    describe: 'Request HTML instead of JSON from server'
}})


yargs.options({
  'nd': {
    default: true,
    alias: 'no-db',
    describe: 'Skips all database loading and checking actions'
}})

yargs.options({
  'ge': {
    default: 0,
    alias: 'get-endpoints',
    describe: 'Directly specific which endpoints to use during GET operations (bypasses id, name, and zip ratios)'
}})

yargs.options({
  'hh': {
    default: "",
    alias: 'http-headers',
    describe: 'Extra HTTP headers to send to the server'
}})

const args = yargs.argv;
console.log('args: ' + args)
console.log('args.id: ' + args.id)
console.log('args.ng: ' + args.ng)
console.log('args.object: ' + args.object)

