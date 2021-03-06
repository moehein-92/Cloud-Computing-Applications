package edu.illinois.storm;

import org.apache.storm.redis.common.mapper.RedisDataTypeDescription;
import org.apache.storm.redis.common.mapper.RedisStoreMapper;
import org.apache.storm.tuple.ITuple;

public class WordCountStoreMapper implements RedisStoreMapper {
  private RedisDataTypeDescription description;
  private final String hashKey;

  public WordCountStoreMapper(String hashKey) {
    this.hashKey = hashKey;
    description =
        new RedisDataTypeDescription(RedisDataTypeDescription.RedisDataType.HASH, hashKey);
  }

  @Override
  public RedisDataTypeDescription getDataTypeDescription() {
    return description;
  }

  @Override
  public String getKeyFromTuple(ITuple tuple) {
    
    return tuple.getStringByField("word");

  }

  @Override
  public String getValueFromTuple(ITuple tuple) {
    
    long count = tuple.getLongByField("count");
    return String.valueOf(count);

  }
}